#include "./ntfy.cpp"
#include <ctime>
#include <iomanip>
#include <iostream>
#include <libpq-fe.h>

using namespace std;

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

int main() {
  PGconn *conn = get_conn();

  time_t now = time(0);
  tm *ltm = localtime(&now);
  std::ostringstream oss;
  oss << std::put_time(ltm, "%B ");
  oss << ltm->tm_mday;
  std::string date = oss.str();

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

  const string b12Str = PQgetvalue(res, 0, 5);
  const string omega3Str = PQgetvalue(res, 0, 6);
  const string kreatinStr = PQgetvalue(res, 0, 7);
  const string abwaschStr = PQgetvalue(res, 0, 8);

  if (b12Str.empty() || omega3Str.empty() || kreatinStr.empty() ||
      abwaschStr.empty()) {
    cerr << "Empty result set\n";
    PQclear(res);
    PQfinish(conn);
    return {};
  }

  PQclear(res);
  PQfinish(conn);

  if (b12Str == "f")
    notifyB12();
  if (omega3Str == "f")
    notifyOmega3();
  if (kreatinStr == "f")
    notifyKreatin();
  if (abwaschStr == "f")
    notifyAbwasch();
}
