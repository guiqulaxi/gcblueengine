#ifndef TCPYTHONBIND_H
#define TCPYTHONBIND_H
#include <pybind11-global/pybind11/pybind11.h>
#include <pybind11-global/pybind11/eval.h>
#include <pybind11-global/pybind11/embed.h>
namespace py = pybind11;
using namespace py;
void BindDBObject(module &m);
void BindDatabase(py::module &m);
#endif // TCPYTHONBIND_H
