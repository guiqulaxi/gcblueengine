#ifndef TCPYTHONBIND_H
#define TCPYTHONBIND_H
#include <pybind11-global/pybind11/pybind11.h>
#include <pybind11-global/pybind11/eval.h>
#include <pybind11-global/pybind11/embed.h>
#include <pybind11-global/pybind11/stl.h>
namespace py = pybind11;
using namespace py;

void BindPlatformInterface(module &m);
void BindPlatformDBInterface(module &m);

void BindDBObject(module &m);
void BindPlatformDBObject(module &m);
void BindTorpedoDBObject(module &m);
void BindMissileDBObject(module &m);
void BindSonobuoyDBObject(module &m);
void BindShipDBObject(module &m);
void BindSubDBObject(module &m);
void BindSpaceDBObject(module &m);
void BindBallisticMissileDBObject( module&m );
void BindDatabase(module &m);
void BindGoal(module &m);
void BindFlightPort(module &m);
void BindScenario(module &m);
void BindSensorDBObject(module &m);
void BindTrack(module &m);
void BindDamageDBObject(module &m);
#endif // TCPYTHONBIND_H
