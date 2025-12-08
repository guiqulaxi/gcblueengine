// ----------------------------------------------------------------------------
// CERTI - HLA RunTime Infrastructure
// Copyright (C) 2002-2005  ONERA
//
// This file is part of CERTI-libCERTI
//
// CERTI-libCERTI is free software ; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public License
// as published by the Free Software Foundation ; either version 2 of
// the License, or (at your option) any later version.
//
// CERTI-libCERTI is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY ; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this program ; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
// USA
//
// ----------------------------------------------------------------------------

#include "Exception.hh"

#include <sstream>

// static members for HLA Exceptions
long network::ArrayIndexOutOfBounds::_type = network::e_ArrayIndexOutOfBounds ;
long network::AsynchronousDeliveryAlreadyDisabled::_type = network::e_AsynchronousDeliveryAlreadyDisabled ;
long network::AsynchronousDeliveryAlreadyEnabled::_type = network::e_AsynchronousDeliveryAlreadyEnabled ;
long network::AttributeAcquisitionWasNotRequested::_type = network::e_AttributeAcquisitionWasNotRequested ;
long network::AttributeAcquisitionWasNotCanceled::_type = network::e_AttributeAcquisitionWasNotCanceled ;
long network::AttributeAlreadyBeingAcquired::_type = network::e_AttributeAlreadyBeingAcquired ;
long network::AttributeAlreadyBeingDivested::_type = network::e_AttributeAlreadyBeingDivested ;
long network::AttributeAlreadyOwned::_type = network::e_AttributeAlreadyOwned ;
long network::AttributeDivestitureWasNotRequested::_type = network::e_AttributeDivestitureWasNotRequested ;
long network::AttributeNotDefined::_type = network::e_AttributeNotDefined ;
long network::AttributeNotKnown::_type = network::e_AttributeNotKnown ;
long network::AttributeNotOwned::_type = network::e_AttributeNotOwned ;
long network::AttributeNotPublished::_type = network::e_AttributeNotPublished ;
long network::ConcurrentAccessAttempted::_type = network::e_ConcurrentAccessAttempted ;
long network::CouldNotDiscover::_type = network::e_CouldNotDiscover ;
long network::CouldNotOpenFED::_type = network::e_CouldNotOpenFED ;
long network::CouldNotRestore::_type = network::e_CouldNotRestore ;
long network::DeletePrivilegeNotHeld::_type = network::e_DeletePrivilegeNotHeld ;
long network::DimensionNotDefined::_type = network::e_DimensionNotDefined ;
long network::EnableTimeConstrainedPending::_type = network::e_EnableTimeConstrainedPending ;
long network::EnableTimeConstrainedWasNotPending::_type = network::e_EnableTimeConstrainedWasNotPending ;
long network::EnableTimeRegulationPending::_type = network::e_EnableTimeRegulationPending ;
long network::EnableTimeRegulationWasNotPending::_type = network::e_EnableTimeRegulationWasNotPending ;
long network::ErrorReadingFED::_type = network::e_ErrorReadingFED ;
long network::EventNotKnown::_type = network::e_EventNotKnown ;
long network::FederateAlreadyExecutionMember::_type = network::e_FederateAlreadyExecutionMember ;
long network::FederateInternalError::_type = network::e_FederateInternalError ;
long network::FederateLoggingServiceCalls::_type = network::e_FederateLoggingServiceCalls ;
long network::FederateNotExecutionMember::_type = network::e_FederateNotExecutionMember ;
long network::FederateOwnsAttributes::_type = network::e_FederateOwnsAttributes ;
long network::FederateWasNotAskedToReleaseAttribute::_type = network::e_FederateWasNotAskedToReleaseAttribute ;
long network::FederatesCurrentlyJoined::_type = network::e_FederatesCurrentlyJoined ;
long network::FederationExecutionAlreadyExists::_type = network::e_FederationExecutionAlreadyExists ;
long network::FederationExecutionDoesNotExist::_type = network::e_FederationExecutionDoesNotExist ;
long network::FederationTimeAlreadyPassed::_type = network::e_FederationTimeAlreadyPassed ;
long network::HandleValuePairMaximumExceeded::_type = network::e_HandleValuePairMaximumExceeded ;
long network::InteractionClassNotDefined::_type = network::e_InteractionClassNotDefined ;
long network::InteractionClassNotKnown::_type = network::e_InteractionClassNotKnown ;
long network::InteractionClassNotPublished::_type = network::e_InteractionClassNotPublished ;
long network::InteractionClassNotSubscribed::_type = network::e_InteractionClassNotSubscribed ;
long network::InteractionParameterNotDefined::_type = network::e_InteractionParameterNotDefined ;
long network::InteractionParameterNotKnown::_type = network::e_InteractionParameterNotKnown ;
long network::InvalidExtents::_type = network::e_InvalidExtents ;
long network::InvalidFederationTime::_type = network::e_InvalidFederationTime ;
long network::InvalidHandleValuePairSetContext::_type = network::e_InvalidHandleValuePairSetContext ;
long network::InvalidLookahead::_type = network::e_InvalidLookahead ;
long network::InvalidOrderingHandle::_type = network::e_InvalidOrderingHandle ;
long network::InvalidRegionContext::_type = network::e_InvalidRegionContext ;
long network::InvalidResignAction::_type = network::e_InvalidResignAction ;
long network::InvalidRetractionHandle::_type = network::e_InvalidRetractionHandle ;
long network::InvalidTransportationHandle::_type = network::e_InvalidTransportationHandle ;
long network::MemoryExhausted::_type = network::e_MemoryExhausted ;
long network::NameNotFound::_type = network::e_NameNotFound ;
long network::ObjectClassNotDefined::_type = network::e_ObjectClassNotDefined ;
long network::ObjectClassNotKnown::_type = network::e_ObjectClassNotKnown ;
long network::ObjectClassNotPublished::_type = network::e_ObjectClassNotPublished ;
long network::ObjectClassNotSubscribed::_type = network::e_ObjectClassNotSubscribed ;
long network::ObjectNotKnown::_type = network::e_ObjectNotKnown ;
long network::ObjectAlreadyRegistered::_type = network::e_ObjectAlreadyRegistered ;
long network::OwnershipAcquisitionPending::_type = network::e_OwnershipAcquisitionPending ;
long network::RegionInUse::_type = network::e_RegionInUse ;
long network::RegionNotKnown::_type = network::e_RegionNotKnown ;
long network::RestoreInProgress::_type = network::e_RestoreInProgress ;
long network::RestoreNotRequested::_type = network::e_RestoreNotRequested ;
long network::RTIinternalError::_type = network::e_RTIinternalError ;
long network::SpaceNotDefined::_type = network::e_SpaceNotDefined ;
long network::SaveInProgress::_type = network::e_SaveInProgress ;
long network::SaveNotInitiated::_type = network::e_SaveNotInitiated ;
long network::SpecifiedSaveLabelDoesNotExist::_type = network::e_SpecifiedSaveLabelDoesNotExist ;
long network::SynchronizationPointLabelWasNotAnnounced::_type = network::e_SynchronizationPointLabelWasNotAnnounced ;
long network::TimeAdvanceAlreadyInProgress::_type = network::e_TimeAdvanceAlreadyInProgress ;
long network::TimeAdvanceWasNotInProgress::_type = network::e_TimeAdvanceWasNotInProgress ;
long network::TimeConstrainedAlreadyEnabled::_type = network::e_TimeConstrainedAlreadyEnabled ;
long network::TimeConstrainedWasNotEnabled::_type = network::e_TimeConstrainedWasNotEnabled ;
long network::TimeRegulationAlreadyEnabled::_type = network::e_TimeRegulationAlreadyEnabled ;
long network::TimeRegulationWasNotEnabled::_type = network::e_TimeRegulationWasNotEnabled ;
long network::UnableToPerformSave::_type = network::e_UnableToPerformSave ;
long network::ValueCountExceeded::_type = network::e_ValueCountExceeded ;
long network::ValueLengthExceeded::_type = network::e_ValueLengthExceeded ;

//  TypeException managing (how to obtain TypeException from Exception name ?)
long network::FederateNotPublishing::_type = network::e_FederateNotPublishing ;
long network::FederateNotSubscribing::_type = network::e_FederateNotSubscribing ;
long network::InvalidObjectHandle::_type = network::e_InvalidObjectHandle ;
long network::CouldNotOpenRID::_type = network::e_CouldNotOpenRID ;
long network::ErrorReadingRID::_type = network::e_ErrorReadingRID ;
long network::AttributeNotSubscribed::_type = network::e_AttributeNotSubscribed ;
long network::FederationAlreadyPaused::_type = network::e_FederationAlreadyPaused ;
long network::FederationNotPaused::_type = network::e_FederationNotPaused ;
long network::SecurityError::_type = network::e_SecurityError ;
long network::FederateAlreadyPaused::_type = network::e_FederateAlreadyPaused ;
long network::FederateDoesNotExist::_type = network::e_FederateDoesNotExist ;
long network::FederateNameAlreadyInUse::_type = network::e_FederateNameAlreadyInUse ;
long network::FederateNotPaused::_type = network::e_FederateNotPaused ;
long network::IDsupplyExhausted::_type = network::e_IDsupplyExhausted ;
long network::InvalidDivestitureCondition::_type = network::e_InvalidDivestitureCondition ;
long network::InvalidFederationTimeDelta::_type = network::e_InvalidFederationTimeDelta ;
long network::InvalidRoutingSpace::_type = network::e_InvalidRoutingSpace ;
long network::NoPauseRequested::_type = network::e_NoPauseRequested ;
long network::NoResumeRequested::_type = network::e_NoResumeRequested ;
long network::TooManyIDsRequested::_type = network::e_TooManyIDsRequested ;
long network::UnimplementedService::_type = network::e_UnimplementedService ;
long network::UnknownLabel::_type = network::e_UnknownLabel ;
long network::NetworkError::_type = network::e_NetworkError ;
long network::NetworkSignal::_type = network::e_NetworkSignal ;
long network::SocketNotConnected::_type = network::e_SocketNotConnected ;
long network::MessageNotSent::_type = network::e_MessageNotSent ;
long network::MessageNotReceived::_type = network::e_MessageNotReceived ;
long network::SocketNotClosed::_type = network::e_SocketNotClosed ;
long network::RingBufferNotCreated::_type = network::e_RingBufferNotCreated ;
long network::RingBufferNotClosed::_type = network::e_RingBufferNotClosed ;
long network::RingBufferNotDeleted::_type = network::e_RingBufferNotDeleted ;
long network::RingBufferNotAttached::_type = network::e_RingBufferNotAttached ;
long network::MessageTooLong::_type = network::e_MessageTooLong ;
long network::BufferFull::_type = network::e_BufferFull ;
long network::BufferEmpty::_type = network::e_BufferEmpty ;
long network::SocketSHMNotCreated::_type = network::e_SocketSHMNotCreated ;
long network::SocketSHMNotOpen::_type = network::e_SocketSHMNotOpen ;
long network::SocketSHMNotDeleted::_type = network::e_SocketSHMNotDeleted ;

long network::IllegalName::_type = network::e_IllegalName ;


const std::string network::Exception::displayMe() const
{
    std::stringstream msg;

    msg << "network::Exception [";
    if (NULL!=_name) {
        msg <<_name;
    } else {
        msg<<"<noname>";
    }
    msg << " - reason=";
    if (!_reason.empty()) {
        msg << _reason;
    } else {
        msg << "<noreason>";
    }
    msg << std::endl;
    msg << std::flush;
    return msg.str();
}
