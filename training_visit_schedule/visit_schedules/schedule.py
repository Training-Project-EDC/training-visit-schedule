from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit
from .crfs import crfs


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


training_subject_visit_schedule = Schedule(
    name='training_subject_visit_schedule',
    verbose_name='Training Visit Schedule',
    onschedule_model='training_subject.onschedule',
    offschedule_model='training_subject.offschedule',
    consent_model='training_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit1 = Visit(
    code='1000',
    title='First Visit',
    timepoint=1,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crfs.get('initial'),
    facility_name='Clinic 1')

visit2 = Visit(
    code='2000',
    title='Second Visit',
    timepoint=2,
    rbase=relativedelta(days=4),
    rlower=relativedelta(days=2),
    rupper=relativedelta(days=2),
    requisitions=None,
    crfs=crfs.get('followup'),
    facility_name='Clinic 1')

training_subject_visit_schedule.add_visit(visit=visit1)
training_subject_visit_schedule.add_visit(visit=visit2)
