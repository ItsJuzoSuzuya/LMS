#include <algorithm>
#include <iostream>
#include <libpq-fe.h>
#include <map>
#include <optional>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>

using namespace std;
using PageData = map<string, string>;

PGconn *get_conn() {
  const char *conn_str =
      "dbname=days user=postgres password=postgres host=0.0.0.0";
  PGconn *conn = PQconnectdb(conn_str);

  if (PQstatus(conn) != CONNECTION_OK) {
    cerr << "Connection failed: " << PQerrorMessage(conn);
    PQfinish(conn);
    return {};
  }

  return conn;
};

PageData get_page(const string &date) {
  PGconn *conn = get_conn();

  string query = "SELECT day, piano, chess, japanese, programming, b12, "
                 "omega3, kreatin, abwasch FROM dayStatus WHERE day = '" +
                 date + "';";
  PGresult *res = PQexec(conn, query.c_str());

  if (PQresultStatus(res) != PGRES_TUPLES_OK) {
    cerr << "SELECT failed: " << PQerrorMessage(conn);
    PQclear(res);
    PQfinish(conn);
    return {};
  }

  if (PQntuples(res) == 0) {
    PQclear(res);
    PQfinish(conn);
    return {};
  }

  PageData pageData;

  const string pianoStr = PQgetvalue(res, 0, 1);
  const string chessStr = PQgetvalue(res, 0, 2);
  const string japaneseStr = PQgetvalue(res, 0, 3);
  const string programmingStr = PQgetvalue(res, 0, 4);
  const string b12Str = PQgetvalue(res, 0, 5);
  const string omega3Str = PQgetvalue(res, 0, 6);
  const string kreatinStr = PQgetvalue(res, 0, 7);
  const string abwaschStr = PQgetvalue(res, 0, 8);


  if (pianoStr.empty() || chessStr.empty() || japaneseStr.empty() ||
      programmingStr.empty() || b12Str.empty() || omega3Str.empty() ||
      kreatinStr.empty() || abwaschStr.empty()) {
    cerr << "Empty result set\n";
    PQclear(res);
    PQfinish(conn);
    return {};
  }

  PQclear(res);
  PQfinish(conn);

  pageData["piano"] = pianoStr;
  pageData["chess"] = chessStr;
  pageData["japanese"] = japaneseStr;
  pageData["programming"] = programmingStr;
  pageData["b12"] = b12Str; 
  pageData["omega3"] = omega3Str;
  pageData["kreatin"] = kreatinStr;
  pageData["abwasch"] = abwaschStr;
  return pageData;
}

void add_page(const string &date, int pianoTime, int chessTime,
              int japaneseTime, int programmingTime) {
  PGconn *conn = get_conn();

  string query =
      "INSERT INTO dayStatus (day, piano, chess, japanese, programming) "
      "VALUES ('" +
      date + "', " + to_string(pianoTime) + ", " + to_string(chessTime) + ", " +
      to_string(japaneseTime) + ", " + to_string(programmingTime) + ");";

  PGresult *res = PQexec(conn, query.c_str());
  if (PQresultStatus(res) != PGRES_COMMAND_OK) {
    cerr << "INSERT failed: " << PQerrorMessage(conn);
    PQclear(res);
    PQfinish(conn);
    return;
  }
  PQclear(res);
  PQfinish(conn);
}

void update_page(const string &date, string &task, optional<int> time,
                 optional<bool> done) {
  PGconn *conn = get_conn();

  if (!time && !done) {
    cerr << "No time or done value provided for update\n";
    return;
  }

  string query;

  if (time)
    query = "UPDATE dayStatus SET " + task + " = " + to_string(time.value()) +
            " WHERE day = '" + date + "';";
  else if (done) {
    string isDone = done.value() ? "TRUE" : "FALSE";
    task.erase(remove_if(task.begin(), task.end(),
                         [](unsigned char c) { return isspace(c); }),
               task.end());

    query = "UPDATE dayStatus SET " + task + " = " + isDone + " WHERE day = '" +
            date + "';";
  }

  PGresult *res = PQexec(conn, query.c_str());
  if (PQresultStatus(res) != PGRES_COMMAND_OK) {
    cerr << "UPDATE failed: " << PQerrorMessage(conn);
    PQclear(res);
    PQfinish(conn);
    return;
  }
  PQclear(res);
  PQfinish(conn);
}

PYBIND11_MODULE(db, m) {
  m.def("get_page", &get_page);
  m.def("add_page", &add_page);
  m.def("update_page", &update_page);
}
