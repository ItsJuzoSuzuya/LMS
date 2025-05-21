#include <cpr/api.h>
#include <cpr/cpr.h>
#include <cpr/response.h>

void notifyB12() {
  cpr::Response r = cpr::Post(cpr::Url{"ntfy.sh/nick_todo_alert"},
                              cpr::Header{{"Content-Type", "application/json"}},
                              cpr::Body{R"(Take B12)"});
}

void notifyOmega3() {
  cpr::Response r = cpr::Post(cpr::Url{"ntfy.sh/nick_todo_alert"},
                              cpr::Header{{"Content-Type", "application/json"}},
                              cpr::Body{R"(Take Omega3)"});
}

void notifyKreatin() {
  cpr::Response r = cpr::Post(cpr::Url{"ntfy.sh/nick_todo_alert"},
                              cpr::Header{{"Content-Type", "application/json"}},
                              cpr::Body{R"(Take Kreatin)"});
}

void notifyAbwasch() {
  cpr::Response r = cpr::Post(cpr::Url{"ntfy.sh/nick_todo_alert"},
                              cpr::Header{{"Content-Type", "application/json"}},
                              cpr::Body{R"(Do the dishes)"});
}

