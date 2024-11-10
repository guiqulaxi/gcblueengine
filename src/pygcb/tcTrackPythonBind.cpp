#include "tcPythonBind.h"
#include "tcTrack.h"

#include <tcPlatformInterface.h>
#include <tcSensorMapTrack.h>
using namespace scriptinterface;
void BindTrack(module &m)
{
    py::class_<tcTrack>(m,"tcTrack")
    .def_readwrite("Alt",&tcTrack::mfAlt_m)
        .def_readwrite("Lat",&tcTrack::mfLat_rad)
        .def_readwrite("Lon",&tcTrack::mfLon_rad)
        .def_readonly("Speed",&tcTrack::mfSpeed_kts)
        .def_readonly("Flags", &tcTrack::mnFlags)
        .def_readonly("Heading_rad",&tcTrack::mfHeading_rad)
        .def_readonly("Bearing_rad", &tcTrack::bearing_rad)
        .def_readonly("BearingRate_radps", &tcTrack::bearingRate_radps)
        .def_readonly("Classification",&tcTrack::mnClassification)
        .def_readonly("Affiliation",&tcTrack::mnAffiliation)
        .def_readonly("ID",&tcTrack::mnID)
        .def_readonly("Time", &tcTrack::mfTimestamp)
        .def("IsAir", &tcTrack::IsAir)
        .def("IsMissile", &tcTrack::IsMissile)
        .def("IsSurface", &tcTrack::IsSurface)
        .def("IsGround", &tcTrack::IsGround)
        .def("IsSub", &tcTrack::IsSub)
        .def("IsTorpedo", &tcTrack::IsTorpedo)
        .def("IsBearingOnly", &tcTrack::IsBearingOnly)
        .def("IsBearingRateValid", &tcTrack::IsBearingRateValid)
        .def("IsValid", &tcTrack::IsValid)
        .def("Offset", &tcTrack::Offset)
        .def("PredictAhead", &tcTrack::PredictAhead)
        ;



    py::class_<tcSensorMapTrack>(m,"tcSMTrack")
        .def_readwrite("Alt",&tcSensorMapTrack::mfAlt_m)
        .def_readwrite("Lat",&tcSensorMapTrack::mfLat_rad)
        .def_readwrite("Lon",&tcSensorMapTrack::mfLon_rad)
        .def_readonly("Speed",&tcSensorMapTrack::mfSpeed_kts)
        .def_readonly("Flags", &tcSensorMapTrack::mnFlags)
        .def_readonly("Heading_rad",&tcSensorMapTrack::mfHeading_rad)
        .def_readonly("Bearing_rad", &tcSensorMapTrack::bearing_rad)
        .def_readonly("BearingRate_radps", &tcSensorMapTrack::bearingRate_radps)
        .def_readonly("Classification",&tcSensorMapTrack::mnClassification)
        .def_readonly("Affiliation",&tcSensorMapTrack::mnAffiliation)
        .def_readonly("ID",&tcSensorMapTrack::mnID)
        .def_readonly("Time", &tcSensorMapTrack::mfTimestamp)
        .def("IsAir", &tcSensorMapTrack::IsAir)
        .def("IsDestroyed", &tcSensorMapTrack::IsDestroyed)
        .def("IsMissile", &tcSensorMapTrack::IsMissile)
        .def("IsSurface", &tcSensorMapTrack::IsSurface)
        .def("IsGround", &tcSensorMapTrack::IsGround)
        .def("IsSub", &tcSensorMapTrack::IsSub)
        .def("IsTorpedo", &tcSensorMapTrack::IsTorpedo)
        .def("IsBearingOnly", &tcSensorMapTrack::IsBearingOnly)
        .def("IsBearingRateValid", &tcSensorMapTrack::IsBearingRateValid)
        .def("IsStale", &tcSensorMapTrack::IsStale)
        .def("IsValid", &tcSensorMapTrack::IsValid)
        .def("Offset", &tcSensorMapTrack::Offset)
        .def("PredictAhead", &tcSensorMapTrack::PredictAhead)
        .def("GetEngagedCount", &tcSensorMapTrack::GetEngagedCount)
        .def("GetEmitterCount", &tcSensorMapTrack::GetEmitterCount)
        .def("GetEmitterInfo",  &tcSensorMapTrack::GetEmitterInfo)
        .def("TrackErrorKm", &tcSensorMapTrack::TrackErrorKm)
        .def("BearingToRad", &tcSensorMapTrack::BearingToRad)
        .def("RangeToKm", &tcSensorMapTrack::RangeToKm)
        .def("GetTrackLife", &tcSensorMapTrack::GetTrackLife)
        ;


    py::class_<tcTrackIterator>(m,"TrackIterator")
        .def_readonly("Alt",&tcTrackIterator::mfAlt_m)
        .def_readonly("Lat",&tcTrackIterator::mfLat_rad)
        .def_readonly("Lon",&tcTrackIterator::mfLon_rad)
        .def_readonly("Speed",&tcTrackIterator::mfSpeed_kts)
        .def_readonly("Heading_rad",&tcTrackIterator::mfHeading_rad)
        .def_readonly("Classification",&tcTrackIterator::mnClassification)
        .def_readonly("Affiliation",&tcTrackIterator::mnAffiliation)
        .def_readonly("ID",&tcTrackIterator::mnID)
        .def_readonly("Key",&tcTrackIterator::mnKey)
        ;

    py::class_<tcTrackList>(m,"TrackList")
        .def("Size",&tcTrackList::Size)
        .def("GetTrack",&tcTrackList::GetTrack)
        ;

}
