#include <iostream>
#include <boost/json/src.hpp>

using namespace std;
namespace bj = boost::json;

int main(void)
{
    bj::object obj1 = {
        {"id", 1},
        {"price", 3343403000000.00},
        {"qty", 13546000000000.00}
    };

    bj::object obj2 = {
        {"id", 2},
        {"price", 0.0},
        {"qty", 0.0}
    };
    cout << "obj1:" << bj::serialize(obj1) << endl;
    cout << "obj2:" << bj::serialize(obj2) << endl;

    return 0;
}