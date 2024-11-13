class data_review_tab:
    def _init_(self):
        self.url = "https://www.google.com/"
        self.miss_spell = "abcd"


class test_timing_data:
    def __init__(self):
        self.two_seconds = 2
        self.five_seconds = 5
        self.ten_seconds = 10
        self.fifteen_seconds = 15


class user_input_data:
    def __init__(self):
        self.patient_first_name = "Michael"
        self.patient_first_name_for_assertion = "Michael"
        self.patient_edit_name = "Michae"
        self.patient_edit_name_for_assertion = "Michaeel"
        self.patient_name_create = "Morbius"
        self.patient_name_edit = "EditName"
        self.patient_name_delete = " "
        self.gender = "male"
        self.gender_f = "female"
        self.patient_genders = ["male", "female"]
        self.patient_ages_format = ["year", "month", "week", "day"]
        self.years_select = "years"
        self.age_format = "year"
        self.age_format_month = "month"
        self.age = "50"
        self.edit_age = "30"
        self.type = ["new", "established"]
        self.age_edit = "35"
        self.age_delete = " "
        self.start_time = "0549P"
        self.start_time_edit = "0341A"
        self.start_time_delete = " "
        self.spent_time = "10"
        self.spent_time_edit = "05"
        self.spent_time_delete = ""
        #self.service_type = "In-person"
        self.unmatch_service_type = "Testing automation"
        self.service_type = ["In-person", "Telehealth", "Phone"]
        self.sub_service_type_of_telehealth = ["Zoom", "Facetime", "Doxy.me", "Epic Canto", "Skype"]
        self.service_type_zoom = "Zoom"
        self.service_type_phone = "Phone"
        self.visit_type = "Acute complaint"
        self.visit_type_after_selected = "Acute complaint (CC)"
        self.search_acute_complaint = "Abdominal pain"
        self.search_chronic_complaint = "Abdominal hernia"
        self.search_complain_abdominal = "Abdominal pain"
        self.search_complain_duplicate = "Annual exam - male"
        self.chief_complaint = "Acne"
        self.complaints_htn = "HTN"
        self.complaints_acute = "Abdominal pain"
        self.complaints_chronic = "Acne"
        self.search_complaints = "Arrhythmia"
        self.complaints_two = "Ear pain"
        self.newcomplaints = "Abdominal"
        self.oldcomplaints = "pain "
        self.wrong_data = "Thisiswrong"
        self.macros = "newmacro"
        self.missspell_data = "Thisismissspell"
        self.build_details = "Pain"
        self.medications_advil_block = "Advil"
        self.medications_no_existed_block = "No_Existed"
        self.autodata = "BTW"
        self.spellchecker = "abcd"
        self.medications = "text"
        self.new_data = "edit"
        self.treatment = "text one"
        self.copy_paste_one = "text one"
        self.copy_paste_two = "text two"
        self.copy_paste_three = "text three"
        self.copy_paste_four = "text four"
        self.timing_selection_first = "constantly"
        self.timing_selection_second = "frequently"
        self.timing_selection_Third = "intermittently"
        self.timing_selection_Fourth = "at night"
        self.complaint_list = ["Acne", "Abdominal pain", "Abscess", "Asthma", "Back Pains",
                               "Depression", "Diabetes", "Eye Symptoms", "GERD", "GI symptoms",
                               "General", "Headache", "Health Maintenance", "Hyperlipidemia", "Insomnia",
                               "Obesity", " Pain", "Rash", "Sleep Apnea", "cough"]
        self.add_macro = "Add macro"
        self.edit_macro = "Edit macro"
        self.add_templates = "This in add templates"
        self.add_auto_correction_title = "ttl"
        self.add_auto_correction_title_edit = "BTW"
        self.add_auto_correction_des = "title"
        self.add_auto_correction_des_edit = "by the way"
        self.edit_dictionary_data = "kemontest"
        self.build_timing_days = "days"
        self.build_enter_time = "20"
        self.click_any_progression_block = "unchanged"
        self.click_any_episode_duration_block = "minutes"
        self.click_any_episode_duration_block_edit = "edit"
        self.notes_test = "text"
        self.quality_select = "aching"
        self.severity_input_one = "0"
        self.severity_input_five = "5"
        self.severity_input_ten = "10"
        self.aggravating_factors_select = "eating"
        self.alleviating_factors_select = "exercise"
        self.complaint_name_one = "Lab follow up"
        self.unmatch_complaint_name = "hhhhh"
        self.red_color_assertion = 'rgba(220, 53, 69, 1)'
        self.change_locator_one_is_active = 'nbtag__item ng-star-inserted nbtag__item--active'
        self.change_locator_two_is_active = 'nbtag_item ng-star-inserted nbtag_item--active'
        self.gender_gray_color = 'rgba(234, 234, 234, 1)'
        self.visit_service_gray_color = 'rgb(234, 234, 234) none repeat scroll 0% 0% / auto padding-box border-box'
        # self.visit_service_gray_color_two = 'rgba(234, 234, 234, 1)'
        self.gender_white_color = 'rgba(0, 0, 0, 0)'
        self.gender_deselect_assertion = 'nbtag__item ng-star-inserted'
        self.patient_genarate_canvas_section = 'The patient is a 50 year old male presenting today for: Annual exam - male.'
        self.performance_blue_color = 'rgba(49, 115, 177, 1)'
        self.spent_time_one_assert = "The patient is a 50 year old male presenting today for: Ear pain. Verbal consent was obtained from the patient to conduct a telehealth video visit via Facetime. I spent 2 minute(s) on Facetime managing this patient."
        self.spent_time_two_assert = "The patient is a 50 year old male presenting today for: Ear pain. Verbal consent was obtained from the patient to conduct a telehealth video visit via Facetime. I spent 10 minute(s) on Facetime managing this patient."
        self.spent_time_three_assert = "The patient is a 50 year old male presenting today for: Ear pain. Verbal consent was obtained from the patient to conduct a telehealth video visit via Facetime. I spent [**] minute(s) on Facetime managing this patient."
        # self.spent_time_three_assert = "The patient is a 50 year old male presenting today for: Abdominal pain. Verbal consent was obtained from the patient to conduct a telehealth video visit via Facetime. I spent [**] minute(s) on Facetime managing this patient."
        self.patient_details = "The patient is a 50 year old male presenting today for: Annual exam - male."
        self.visit_type_gray_color = 'rgba(234, 234, 234, 1)'
        self.visit_type_deselect_locator = 'nbtag__item ng-star-inserted'
        self.white_color_two = 'rgba(0, 0, 0, 0)'
        self.visit_service_gray_color_two = 'rgba(234, 234, 234, 1)'
        self.deselect_assertion = 'nbtag__item ng-star-inserted'
        self.white_color_three = 'rgba(0, 0, 0, 0)'
        self.delete_icon_class = "nbtag__icon__delete ng-star-inserted"
        self.delete_icon_class_two = "nbtag_icon_delete ng-star-inserted"
        self.are_you_sure_assert = "Are you sure you want to delete this template and it's content?"
        self.onset_textfiled_canvas_assert1 = "He reports onset 20."
        self.onset_textfiled_canvas_assert2 = "The patient reports onset 20."
        self.onset_textfiled_canvas_assert3 = "He reports onset 10."
        self.onset_textfiled_canvas_assert4 = "The patient reports onset 10."
        self.onset_textfiled_canvas_assert5 = "He reports onset hours ago."
        self.onset_textfiled_canvas_assert6 = "The patient reports onset hours ago."
        self.timing_canvas_assert = "The symptoms occur at night."
        self.timing_canvas_assert2 = "The symptoms occur in the morning and at night."
        self.progressio_canvas_assert = "He reports the symptoms are unchanged."
        self.progressio_canvas_assert2 = "The patient reports the symptoms are unchanged."
        self.click_any_progression_block2 = "worsening"
        self.episode_duration_canvas_assert = "He reports episodes last minutes."
        self.episode_duration_canvas_assert2 = "He states episodes last minutes."
        self.episode_duration_canvas_assert3 = "The patient reports episodes last minutes."
        self.episode_duration_canvas_assert4 = "He reports episodes last days."
        self.episode_duration_canvas_assert5 = "He states episodes last days."
        self.episode_duration_canvas_assert6 = "The patient states episodes last days."
        self.episode_duration_canvas_assert7 = "The patient reports episodes last days."
        self.episode_duration_canvas_assert8 = "He reports episodes last minutes."
        self.episode_duration_canvas_assert9 = "He states episodes last minutes."
        self.episode_duration_canvas_assert10 = "The patient states episodes last minutes."
        self.episode_duration_canvas_assert11 = "The patient reports episodes last minutes."
        self.phn_spent_time = "The patient is a 50 year old male presenting today for: Ear pain. Verbal consent was obtained from the patient to conduct a phone visit. I spent 10 minute(s) on the phone managing this patient."

        self.under_hpi_first_sentence = "The patient is a 50 year old male presenting today for: Annual exam - male."

        self.description_quality_acing_canvas = "He describes his pain as aching."
        self.description_quality_acing_canvas2 = "He describes his symptoms as aching."
        self.description_quality_acing_canvas3 = "The patient describes his symptoms as aching."



        from selenium.webdriver.common.by import By

        self.Input_Hpi = (
        By.XPATH, "//*[@class='nbcanvas-sentence nbcanvas-sentence--secondary nbcanvas-sentence--focused']")
        self.ROS_click_text_Box = (
            By.XPATH, "//*[@class='nbcanvas-sentence nbcanvas-sentence--secondary nbcanvas-sentence--focused']")
        self.input_AP_text_Box = (
            By.XPATH, "//*[@class='nbcanvas-sentence nbcanvas-sentence--secondary nbcanvas-sentence--focused']")
        self.PE_TextBox_Input = (
            By.XPATH, "//*[@class='nbcanvas-sentence nbcanvas-sentence--secondary nbcanvas-sentence--focused']")
        self.RichText_Editor = (By.XPATH, '//*[@id="richtexteditor"]')
        self.google_searchbtn = (By.XPATH, '//*[@name="q"]')
