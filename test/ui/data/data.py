import pytest
from utils import helper

class Data:
    def __init__(self):
        self.home_screen_provider = pytest.configs.get_config('home_screen_provider')
        self.password_reset_provider = pytest.configs.get_config('password_reset_provider')
        self.appointment_provider = 'test_ed_ui_appointment_screen_provider01@augmedix.com' #pytest.configs.get_config('appointment_provider')
        self.feedback_provider = pytest.configs.get_config('feedback_provider')
        self.archive_provider = pytest.configs.get_config('archive_provider')
        self.background_provider = pytest.configs.get_config('background_provider')
        self.go_ed_module_provider = pytest.configs.get_config('go_ed_module_provider')
        self.remove_upload_provider = pytest.configs.get_config('remove_upload_provider')
        self.basic_behavior_provider = pytest.configs.get_config('basic_behavior_provider')
        self.basic_behavior_provider2 = pytest.configs.get_config('basic_behavior_provider2')
        self.basic_behavior_part2_provider = pytest.configs.get_config('basic_behavior_part2_provider')
        self.basic_behavior_part3_provider = pytest.configs.get_config('basic_behavior_part3_provider')
        self.basic_behavior_part4_provider = pytest.configs.get_config('basic_behavior_part4_provider')
        self.provider_password_in_bullet = '•••••••••'
        self.test_provider = pytest.configs.get_config('test_provider')
        self.ed_specialty_disabled_provider = pytest.configs.get_config('ed_specialty_disabled_provider')
        self.ehr_true_upload_false_provider = pytest.configs.get_config('ehr_true_upload_false_provider')
        self.ehr_true_upload_false_provider_npi = pytest.configs.get_config('ehr_true_upload_false_provider_npi')
        self.ehr_true_upload_true_provider = pytest.configs.get_config('ehr_true_upload_true_provider')
        self.password_all = '#UgMed1x@'
        self.ehr_true_upload_true_provider_npi = pytest.configs.get_config('ehr_true_upload_true_provider_npi')
        self.ehr_true_upload_false_provider2 = pytest.configs.get_config('ehr_true_upload_false_provider2')
        self.ehr_true_upload_false_provider2_npi = pytest.configs.get_config('ehr_true_upload_false_provider2_npi')
        self.note_customer_email_non_ehr = pytest.configs.get_config('note_customer_email_non_ehr')
        self.multiple_recording_provider = pytest.configs.get_config('multiple_recording_provider')
        self.provider_password = pytest.configs.get_config('provider_password')
        self.ehr_provider_password = pytest.configs.get_config('ehr_provider_password')

        self.home_screen_scribe = pytest.configs.get_config('home_screen_scribe')
        self.password_reset_scribe = pytest.configs.get_config('password_reset_scribe')
        self.appointment_scribe = pytest.configs.get_config('appointment_scribe')
        self.feedback_scribe = pytest.configs.get_config('feedback_scribe')
        self.test_scribe = pytest.configs.get_config('test_scribe')
        self.ed_specialty_disabled_scribe = pytest.configs.get_config('ed_specialty_disabled_scribe')
        self.archive_scribe = pytest.configs.get_config('archive_scribe')
        self.background_scribe = pytest.configs.get_config('background_scribe')
        self.go_ed_module_scribe = pytest.configs.get_config('go_ed_module_scribe')
        self.remove_upload_scribe = pytest.configs.get_config('remove_upload_scribe')
        self.basic_behavior_scribe = pytest.configs.get_config('basic_behavior_scribe')
        self.basic_behavior_part2_scribe = pytest.configs.get_config('basic_behavior_part2_scribe')
        self.basic_behavior_part3_scribe = pytest.configs.get_config('basic_behavior_part3_scribe')
        self.basic_behavior_part4_scribe = pytest.configs.get_config('basic_behavior_part4_scribe')
        self.multiple_recording_scribe = pytest.configs.get_config('multiple_recording_scribe')

        self.scribe_password = pytest.configs.get_config('scribe_password')
        self.test_password = pytest.configs.get_config('test_password')

        self.transcript_customer_email_non_ehr = pytest.configs.get_config('ed_transcript_customer_email')
        self.transcript_customer_password_non_ehr = pytest.configs.get_config('password_for_all')

        self.visit_customer_email = pytest.configs.get_config('visit_customer_email')
        self.visit_customer_password = pytest.configs.get_config('password_for_all')

        self.account_blocked_email = pytest.configs.get_config('account_blocked_customer_email')
        self.password_expired_email = pytest.configs.get_config('password_expired_customer_email')
        self.password_expired_password = pytest.configs.get_config('password_expired_customer_password')



        self.daily_check_in_text = 'Daily Check-in'
        self.rate_your_experience_text = 'Rate your experience'
        self.augmedix_go_help_text = 'Augmedix Go helped you save time on your shift by:'
        self.augmedix_go_releive_text = 'Augmedix Go relieves the cognitive load of documentation.'
        self.strong_disagree_text = 'Strong Disagree'
        self.strong_agree_text = 'Strong Agree'
        self.others_text = 'Other feedback'
        self.send_button_text = 'Send'
        self.text_feedback_textarea_default_text = 'Type here...'


        
        self.visit_name = 'Test Sanity Note'
        self.INSTRUCTION_TEXT = 'Enter your email. We’ll send you a link to reset your password.'
        self.DONT_HAVE_AN_ACCOUNT_TEXT = "Don't have account?"
        self.SIGNUP_FIRST_NAME = 'Random'
        self.SIGNUP_LAST_NAME = 'Name'
        self.SIGNUP_WORK_EMAIL = f'test_{helper.generate_random_alphanumeric_string(4)}@random.com'
        self.SIGNUP_NPI_NUMBER = '1245319599'
        self.SIGNUP_PHONE_NUMBER = '(013) 746-2836'
        self.ATHENA_PRAC_ID = '123'
        self.PRACTICE_NAME = 'Random'
        self.BUSINESS_ADDRESS = 'Florida/Alaska'
        self.ZIP_CODE = '3533'
        self.ACCOUNT_INITIATED_TEXT = 'Account initiated'
        self.ACCOUNT_INITIATED_TEXT_MSG = 'An Augmedix team member will be reaching out within 1 business day to help with next steps.'
        self.HOME_SCREEN_PROVIDER_NAME = 'Random Name'
        self.PASSCODE_SCREEN_RESET_LINK_TEXT = '(Not you? Tap here to change.)'
        self.INCORRECT_PIN_TEXT = 'Incorrect PIN'
        self.SHORT_AUDIO_PATIENT_NAME = 'Short Patient'
        self.LONG_AUDIO_PATIENT_NAME = 'Long Patient'
        self.TRACKER_ARCHIVE_PATIENT_NAME = f'Tracker Patient'
        self.TODO_ARCHIVE_PATIENT_NAME = 'TODO Patient'
        self.NOTE_STATUS_1_PATIENT_NAME = 'Note Status 1'
        self.NOTE_STATUS_4_PATIENT_NAME = 'Note Status 4'
        self.NOTE_STATUS_9_PATIENT_NAME = 'Note Status 9'
        self.RESTORE = 'Restore'
        self.ARCHIVE = 'Archive'
        self.SHORT_PATIENT_EDIT_ADD_NAME = 'Short Patient Add'
        self.ADD_TEXT_TO_NOTE = "Hello. This is some texts being added to the generated note."
        self.SCP_PATIENT_EDIT_REMOVE_NAME = 'SCP Remove Patient'
        self.NO_EDIT_PATIENT_NAME = 'No Edit Patient'
        self.NO_EDIT_PATIENT_2_NAME = 'No Edit Patient 2'
        self.MDM_PATIENT_NAME = 'MDM_Patient'
        self.MDM_DISABLED_PATIENT_NAME = 'AP Patient'
        self.RE_EVAL_PATIENT_NAME = 'Re_Eval_Patient'
        self.CURRENT_TIME_PARTIAL = f'Time '
        self.RE_EVAL_BUTTON_TEXT = '+ Add Re-eval'
        self.RE_EVAL_TIMESTAMP = f'Time {helper.get_date_time_by_zone(date_format="%I:",_timezone="America/New_York").lstrip("0")}'
        self.RE_EVAL_PATIENT_2_NAME = 'Re_Eval_Patient2'
        self.RE_EVAL_PATIENT_3_NAME = 'Re_Eval_Patient3'
        self.MULTIPLE_RECORDING_PATIENT1_NAME = 'Multiple_Recording_Patient1'
        self.TRANSCRIPT_PATIENT1_NAME = 'Transcript Patient1'
        self.TRANSCRIPT_PATIENT2_NAME = 'Transcript Patient2'
        self.FIRST_RE_EVAL_HEADER_TEXT = 'Progress #1'
        self.SECOND_RE_EVAL_HEADER_TEXT = 'Progress #2'
        self.THIRD_RE_EVAL_HEADER_TEXT = 'Progress #3'
        self.FIRST_RE_EVAL_TEXT = 'Texts being added to first re-eval'
        self.SECOND_RE_EVAL_TEXT = 'Texts being added to second re-eval'
        self.THIRD_RE_EVAL_TEXT = 'Texts being added to third re-eval'
        self.FIRST_PATIENT_NAME = 'First Patient'
        self.SECOND_PATIENT_NAME = 'Second Patient'
        self.THIRD_PATIENT_NAME = 'Third Patient'
        self.REMOVE_UPLOAD_PATIENT_NAME = 'Remove Upload Patient'
        self.ADD_CONTENT_PATIENT_NAME = 'Add Content Patient'
        self.EHR_PATIENT_NAME = 'EHR Patient'
        self.GO_ED_PATIENT_NAME = 'ED Patient'
        self.EHR_JENKINS_PATIENT_NAME = 'Test Automation'
        self.CHIEF_COMPLAINT = 'Nausea'
        self.MULTIPLE_CHIEF_COMPLAINTS = 'Nausea,Asthma,Headache,Palpitation,Hypertension,Diabetes'
        self.THREE_DIGIT_ROOM_NUMBER = '101'
        self.AGE_AND_SEX = '24, M'
        self.TRANSCRIPT_PATIENT_NAME = 'Transcripts Patient'
        self.ONBOARDING_PIN_TEXT = "Your PIN will allow quick access to the app after inactivity. For your security, you'll need to re-enter your password every 12 hours."
        self.ONBOARDING_PIN_HEADER_TEXT = 'Create a PIN'
        self.set_password_header = 'Set Password'
        self.reset_password = 'Augmedix@126'

        self.TRANSCRIPT_PATIENT_MULTILINGUAL_NAME = 'Multilingual Transcripts'
        self.FIRST_LINE_TRANSCRIPT_TEXT = 'Hey. How are you doing?'
        self.LAST_LINE_TRANSCRIPT_TEXT = 'Thank you.'
        self.SEARCH_TEXT = 'metformin'
        self.DELETE_RECORDING_MESSAGE = 'Recording audio and content will be permanently deleted for the selected transcript.'
        self.AUDIO_FILES = ['utils/upload_go_audio/HIMMS_Demo_Recording_1st_52_seconds.mp4',
                 'utils/upload_go_audio/HIMMS_Demo_Recording_2nd_part.mp4',
                 'utils/upload_go_audio/HIMMS_Demo_Recording_3rd_part.mp4']
        self.AUDIO_FILES_SPANISH = ['utils/upload_go_audio/Medical_Spanish_Mock.mp4']
        self.MANUALLY_UPDATE_NOTE_TEXT = " Update patient info "
        self.HPI_SENTENCE_INSTRUCTION_MODAL ={
            "title": "Sentence Style Example",
            "concise_title": "Concise",
            "concise_value": "Educational material was provided to patient. The Patient acknowledged understanding "
                             "and receipt of educational content.",
            "narrative_title": "Narrative",
            "narrative_value": "The patient received educational material specific to their symptoms and "
                               "prescribed HPI. The Patient acknowledged understanding and receipt of educational "
                               "content to review, and will follow at home as prescribed."
        }
        self.MDM_SENTENCE_INSTRUCTION_MODAL ={
            "title": "Sentence Style Example",
            "concise_title": "Concise",
            "concise_value": "Educational material was provided to patient. The Patient acknowledged understanding "
                             "and receipt of educational content.",
            "narrative_title": "Narrative",
            "narrative_value": "The patient received educational material specific to their symptoms and "
                               "prescribed MDM. The Patient acknowledged understanding and receipt of educational "
                               "content to review, and will follow at home as prescribed."
        }
        self.PASSCODE_CONFIRM_SCREEN_PROVIDER_NAME = 'test_ed_ui_ home_screen_provider01'
        self.FIRST_INCORRECT_PASSCODE_MESSAGE_TEXT = '2 attempts left, then forced relogin'
        self.SECOND_INCORRECT_PASSCODE_MESSAGE_TEXT = '1 attempts left, then forced relogin'
        self.ENGLISH_LANGUAGE_CODE = 'EN'
        self.SPANISH_LANGUAGE_CODE = 'ES'
        self.ONBOARDING_PIN_TEXT = "Your PIN will allow quick access to the app after inactivity. For your security, you'll need to re-enter your password every 12 hours."
        self.ONBOARDING_PIN_HEADER_TEXT = 'Create a PIN'
        self.set_password_header = 'Set Password'
        self.reset_password = 'Augmedix@126'


    # Problems
    ACUTE_PROBLEMS_NAME = 'Abdominal pain'
    CHRONIC_PROBLEM_NAME = 'Diabetes, Type 2'
    CHRONIC_PROBLEM_HYPERTENSION = 'Hypertension'
    # HPI Symptoms
    ACUTE_HPI_SYMPTOMS_NAME = ''
    CHRONIC_HPI_SYMPTOMS_NAME = 'urinary frequency'
    CHRONIC_HPI_SYMPTOMS = {
            'name': 'urinary frequency',
            'name_note': 'Patient complains of  urinary frequency.'
        }
    HYPERTENSION_HPI_SYMPTOMS_NAME = 'hair thinning'
    HYPERTENSION_HPI_SYMPTOMS_NOTE = 'Patient complains of associated hair thinning.'
    # HPI Current medications
    ACUTE_HPI_CURRENT_MEDICATION_NAME = 'pantoprazole'
    CHRONIC_HPI_CURRENT_MEDICATION_NAME = 'metformin'
    CHRONIC_HPI_CURRENT_MEDICATION_DOSAGE = '500 mg'
    CHRONIC_HPI_CURRENT_MEDICATION_FREQUENCY = "BID"
    CHRONIC_HPI_CURRENT_MEDICATION = {
            'name': 'metformin',
            'name_note': "Patient's current medications include: metformin.",
            'dosage': '500 mg',
            'dosage_note': "Patient's current medications include: metformin 500 mg.",
            'frequency': 'BID',
            'frequency_note': "Patient's current medications include: metformin BID.",
            'frequency_note_with_dosage': "Patient's current medications include: metformin 500 mg BID."
        }

    HYPERTENSION_HPI_CURRENT_MEDICATION_NAME = 'buspirone'
    HYPERTENSION_HPI_CURRENT_MEDICATION_NOTE = "Patient's current medications include: buspirone 15 mg QD."
    # HPI Lifestyle treatments
    ACUTE_HPI_LIFESTYLE_TREATMENT_NAME = 'avoiding spicy foods'
    CHRONIC_HPI_LIFESTYLE_TREATMENT_NAME = 'regular exercise'
    CHRONIC_HPI_LIFESTYLE_TREATMENT_DETAILS = 'at least for 60 minutes'
    CHRONIC_HPI_LIFESTYLE_TREATMENT = {
            'name': 'regular exercise',
            'name_note': 'Lifestyle modification includes regular exercise.',
            'detail': 'at least for 60 minutes',
            'detail_note': 'Lifestyle modification includes regular exercise at least for 60 minutes.'
        }
    HYPERTENSION_HPI_LIFESTYLE_TREATMENT_NAME = 'exercise'
    HYPERTENSION_HPI_LIFESTYLE_TREATMENT_NOTE = 'Lifestyle treatments include exercise.'
    # HPI Treatment procedures
    ACUTE_HPI_TREATMENT_PROCEDURE_NAME = 'above knee amputation'
    CHRONIC_HPI_TREATMENT_PROCEDURE_NAME = 'angiography'
    CHRONIC_HPI_TREATMENT_PROCEDURE = {
            'name': 'angiography',
            'name_note': 'Patient has been treated with angiography.',
            'relief': 'with relief',
            'relief_note': 'Patient has been treated with angiography with relief.'
        }
    # HPI Recent Labs
    CHRONIC_HPI_RECENT_LAB_NAME = 'Lipid panel'
    CHRONIC_HPI_RECENT_LAB_VALUE = '8'
    CHRONIC_HPI_RECENT_LAB_IMPRESSION_VALUE = 'normal'
    CHRONIC_HPI_RECENT_LAB_DATE = '2023-01-02'
    CHRONIC_HPI_RECENT_LAB = {
            'name': 'Lipid panel',
            'name_note': 'Lipid panel.',
            'value': '8',
            'value_note': 'Lipid panel at 8.',
            'impression': 'normal',
            'impression_note': 'Lipid panel normal.',
            'impression_note_with_value': 'Lipid panel normal at 8.',
            'date': '2023-01-02',
            'date_note': 'Lipid panel on 01-02-2023.',
            'date_note_with_value': 'Lipid panel at 8 on 01-02-2023.',
            'date_note_with_impression': 'Lipid panel normal on 01-02-2023.',
            'date_note_with_value_impression': 'Lipid panel normal at 8 on 01-02-2023.'
        }
    HYPERTENSION_HPI_RECENT_LAB_NAME = 'Microalbumin'
    HYPERTENSION_HPI_RECENT_LAB_NOTE = 'Microalbumin normal.'
    # HPI Recent imaging
    CHRONIC_HPI_RECENT_IMAGING_NAME = 'US Abdomen'
    CHRONIC_HPI_RECENT_IMAGING = {
            'name': 'US Abdomen',
            'name_note': 'US Abdomen was performed.',
            'findings': '4.3',
            'findings_note': 'US Abdomen was performed and revealed 4.3.',
            'impression': 'normal',
            'impression_note': 'US Abdomen was performed which was normal.',
            'impression_note_with_findings': 'US Abdomen was performed which was normal and revealed 4.3.',
            'date': '2022-12-04',
            'date_note': 'US Abdomen was performed on 12-04-2022.',
            'date_note_with_findings': 'US Abdomen was performed on 12-04-2022 and revealed 4.3.',
            'date_note_with_impression': 'US Abdomen was performed on 12-04-2022 which was normal.',
            'date_note_with_findings_impression': 'US Abdomen was performed on 12-04-2022 which was normal and revealed 4.3.'
        }
    # HPI Recent diagnostics
    CHRONIC_HPI_RECENT_DIAGNOSTIC_NAME = 'angiogram'
    CHRONIC_HPI_RECENT_DIAGNOSTIC = {
            'name': 'angiogram',
            'name_note': 'Angiogram was performed.',
            'findings': '7.2',
            'findings_note': 'Angiogram was performed revealing 7.2.',
            'impression': 'abnormal',
            'impression_note': 'Angiogram was performed which was abnormal.',
            'impression_note_with_findings': 'Angiogram was performed which was abnormal revealing 7.2.',
            'date': '2023-01-03',
            'date_note': 'Angiogram was performed on 01-03-2023.',
            'date_note_with_findings': 'Angiogram was performed on 01-03-2023 revealing 7.2.',
            'date_note_with_impression': 'Angiogram was performed on 01-03-2023 which was abnormal.',
            'date_note_with_findings_impression': 'Angiogram was performed on 01-03-2023 which was abnormal revealing 7.2.'
        }

    HYPERTENSION_HPI_RECENT_DIAGNOSTIC_NAME = 'ECG'
    HYPERTENSION_HPI_RECENT_DIAGNOSTIC_NOTE = 'ECG was performed.'
    # Status
    CHRONIC_AP_STATUS_NAME = 'new'
    CHRONIC_AP_STATUS = {
            'name': 'new',
            'name_note': 'New, chronic.'
        }
    ACUTE_AP_STATUS_NAME = 'established'
    HYPERTENSION_AP_STATUS_NAME = 'established'
    HYPERTENSION_AP_STATUS_NOTE = 'Established, chronic.'
    # Progression
    CHRONIC_AP_PROGRESSION_NAME = 'uncontrolled'
    CHRONIC_AP_PROGRESSION = {
            'name': 'uncontrolled',
            'name_note': 'Uncontrolled.'
        }
    ACUTE_AP_PROGRESSION_NAME = 'stable'
    HYPERTENSION_AP_PROGRESSION_NAME = 'improving'
    HYPERTENSION_AP_PROGRESSION_NOTE = 'Improving.'
    # Medications
    CHRONIC_AP_MEDICATION_NAME = 'Levemir'
    CHRONIC_AP_MEDICATION = {
            'name': 'Levemir',
            'name_note': 'I advised the patient to: Levemir.',
            'action': 'start',
            'action_note': 'I advised the patient to: start Levemir.',
            'dosage': '100 unt/ml',
            'dosage_note': 'I advised the patient to: Levemir 100 unt/ml.',
            'dosage_note_with_action': 'I advised the patient to: start Levemir 100 unt/ml.',
            'frequency': 'QD',
            'frequency_note': 'I advised the patient to: Levemir QD.',
            'frequency_note_with_action': 'I advised the patient to: start Levemir QD.',
            'frequency_note_with_dosage': 'I advised the patient to: Levemir 100 unt/ml QD.',
            'frequency_note_with_action_dosage': 'I advised the patient to: start Levemir 100 unt/ml QD.'

        }
    ACUTE_AP_MEDICATION_NAME = 'tramadol'
    HYPERTENSION_AP_MEDICATION_NAME = 'Anafranil'
    HYPERTENSION_AP_MEDICATION_NOTE = 'I advised the patient to: start Anafranil 25 mg QD.'
    # Lifestyle treatments
    CHRONIC_AP_LIFESTYLE_TREATMENT_NAME = 'healthy diet'
    CHRONIC_AP_LIFESTYLE_TREATMENT = {
            'name': 'healthy diet',
            'name_note': 'I recommended: healthy diet.',
            'detail': 'from given chart',
            'detail_note': 'I recommended: healthy diet from given chart.'
        }
    ACUTE_AP_LIFESTYLE_TREATMENT_NAME = 'BRAT diet'
    HYPERTENSION_AP_LIFESTYLE_TREATMENT_NAME = 'low-carb diet'
    HYPERTENSION_AP_LIFESTYLE_TREATMENT_NOTE = 'I recommended lifestyle modification: low-carb diet.'
    # Treatment procedure
    CHRONIC_AP_TREATMENT_PROCEDURE_NAME = 'adenoidectomy'
    CHRONIC_AP_TREATMENT_PROCEDURE = {
            'name': 'adenoidectomy',
            'name_note': 'I recommended the patient pursue adenoidectomy.',
            'opinion': 'agreed',
            'opinion_note': 'I recommended the patient pursue adenoidectomy, patient agreed.',
            'detail': 'regularly',
            'detail_note': 'I recommended the patient pursue adenoidectomy regularly.',
            'detail_note_with_opinion': 'I recommended the patient pursue adenoidectomy regularly, patient agreed.'
        }
    ACUTE_AP_TREATMENT_PROCEDURE_NAME = 'above knee amputation'
    # Lbs
    CHRONIC_AP_LAB_NAME = 'BUN'
    CHRONIC_AP_LAB = {
            'name': 'BUN',
            'name_note': 'Ordered BUN.',
            'detail': 'in office today',
            'detail_note': 'Ordered BUN to be completed in office today.'
        }
    ACUTE_AP_LAB_NAME = 'Hemoccult'
    HYPERTENSION_AP_LAB_NAME = 'Lipid panel'
    HYPERTENSION_AP_LAB_NOTE = 'I ordered the following labs:  Lipid panel to be completed in office today.'
    # Imaging
    CHRONIC_AP_IMAGING_NAME = 'CT Leg'
    CHRONIC_AP_IMAGING = {
            'name': 'CT Leg',
            'name_note': 'I have ordered: CT Leg.',
            'imaging': 'perform asap',
            'imaging_note': 'I have ordered: CT Leg perform asap.'
        }
    ACUTE_AP_IMAGING_NAME = 'US Abdomen'
    # Diagnostic procedures
    CHRONIC_AP_DIAGNOSTIC_PROCEDURE_NAME = 'genetic testing'
    CHRONIC_AP_DIAGNOSTIC_PROCEDURE = {
            'name': 'genetic testing',
            'name_note': 'I have ordered the following diagnostic procedures: genetic testing.',
            'diagnostic': 'complete before next meeting',
            'diagnostic_note': 'I have ordered the following diagnostic procedures: genetic testing complete before next meeting.'
        }
    ACUTE_AP_DIAGNOSTIC_PROCEDURE_NAME = 'amniocentesis'
    HYPERTENSION_AP_DIAGNOSTIC_PROCEDURE_NAME = 'EEG'
    HYPERTENSION_AP_DIAGNOSTIC_PROCEDURE_NOTE = 'I have ordered the following diagnostic procedures: EEG.'

    # DB query
    PASSWORD_EXPIRED_QUERY = f"UPDATE `doctor` SET `doctorPasswordResetDate` = '2022-01-11 08:49:39' WHERE (`doctorEmail` = '##doctorEmail##')"
    UPDATE_DOCTOR_STATUS_QUERY = f"UPDATE `doctor` SET `doctorStatus` = '##doctorStatus##' WHERE (`doctorEmail` = '##doctorEmail##')"
    DOCTOR_EMAIL_PLACEHOLDER = "##doctorEmail##"
    DOCTOR_STATUS_PLACEHOLDER = "##doctorStatus##"

    # Error messages
    PASSWORD_EXPIRED_ERROR_MSG = 'Your Password has expired. Please reset your password, and continue.'

    NOTE_UPLOADED_SUCCESSFULLY_MESSAGE = 'Note has uploaded successfully to your EHR. Please review and sign off.'
    NOTE_UPLOADED_FAILED_MESSAGE = 'Note failed to upload. Please try again.'

    ACCOUNT_BLOCKED_ERROR_MSG = 'You’ve exceeded the maximum number of login attempts. To unlock your account, please reset your password.'
