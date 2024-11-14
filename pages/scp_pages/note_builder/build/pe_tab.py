"""Page object for PE"""
import random

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PeTab(BasePage):
    """Page object for PE"""
    PE_TAB = (By.XPATH, '//span[contains(text(),\'PE\')]')
    PE_LIST_OF_SECTIONS = (By.XPATH, '//app-nb-pe//section')
    PE_CANVAS_SECTION = (By.XPATH, '(//div[@class="nbcanvas-sentence__list"])[4]')
    PE_BLOCK_HEADER_AND_TEXT = (
        By.XPATH,
        '//app-nb-pe-group/section//span[@data-ui-nb-preview-text] | //div[@class=\'nbblock__item__header__hl\']',
    )
    PE_UNLOCK_MODAL_YES_BUTTON = (By.XPATH, '//app-nb-modal//button[text()=\'Yes\']')
    PRESET_SAVE_BUTTON = (
        By.XPATH,
        '//li[contains(@class,\'nbselect__list__item\') and text()=\'Save\']',
    )
    PRESET_SAVE_AS_NEW_BUTTON = (
        By.XPATH,
        '//li[contains(@class,\'nbselect__list__item\') and text()=\'Save as new\']',
    )
    PE_PRESET_TOAST = (By.ID, 'ajs-provider-toast-0')
    PE_LIST_OF_FREE_TEXT_INPUTS = (
        By.XPATH,
        '//app-nb-pe-block-free-text//div[@class=\'nbblock__item__list__item__input\']',
    )
    MODAL_TITLE = (By.CLASS_NAME, 'nbmodal__content__title')
    MODAL_CONTENT = (By.CLASS_NAME, 'nbmodal__content__body')
    BLOCK_ELEMENTS = (By.XPATH, '//app-nb-pe-row//span')
    CLEAR_MODAL_TEXT = (By.XPATH, '//app-nb-modal//text()')
    CANCEL_BUTTON = (By.XPATH, '//button[text()=\'Cancel\']')
    CROSS_ICON = (By.XPATH, '//button[@class=\'nbmodal__content__close\']')
    PE_FREE_TEXT_1 = (
        By.XPATH,
        '(//app-nb-pe-block-free-text//div[@class=\'nbblock__item__list__item__input\'])[1]',
    )
    PE_FREE_TEXT_2 = (
        By.XPATH,
        '(//app-nb-pe-block-free-text//div[@class=\'nbblock__item__list__item__input\'])[2]',
    )
    PE_FREE_TEXT_3 = (
        By.XPATH,
        '(//app-nb-pe-block-free-text//div[@class=\'nbblock__item__list__item__input\'])[3]',
    )
    PE_SECTION_LOCATOR = (By.XPATH, '//app-nb-pe-group/section')
    PE_SECTION_INPUT_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-group)[1]//app-nb-pe-block-header',
    )
    PE_SECTION_OPTION_LOCATOR = (By.XPATH, '(//app-nb-pe-group)[1]//app-nb-pe-row')
    PE_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input.nbblock__item__header__checkbox')

    '''General locators'''

    ABNORMAL_LIST1_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-row[1]//app-nb-descriptor)[2]//li/span',
    )
    ABNORMAL_LIST2_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-row[2]//app-nb-descriptor)[2]//li/span',
    )
    ABNORMAL_LIST3_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-row[3]//app-nb-descriptor)[2]//li/span',
    )
    ABNORMAL_LIST4_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-row[4]//app-nb-descriptor)[2]//li/span',
    )
    ABNORMAL_LIST5_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-row[5]//app-nb-descriptor)[2]//li/span',
    )
    ABNORMAL_LIST6_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-row[6]//app-nb-descriptor)[2]//li/span',
    )
    ABNORMAL_LIST7_LOCATOR = (
        By.XPATH,
        '(//app-nb-pe-row[7]//app-nb-descriptor)[2]//li/span',
    )

    NORMAL_LIST_LOCATOR = (By.XPATH, '//app-nb-single-select//span')

    '''
    Test Data
    '''
    '''
        Block - General
    '''
    GENERAL_NORMAL_1 = 'well appearing'
    GENERAL_NORMAL_2 = 'well developed'
    GENERAL_NORMAL_3 = 'well nourished'
    GENERAL_ABNORMAL_LIST1 = [
        'acute distress',
        'lethargy',
        'sleeping',
        'ill appearance',
        'toxic appearance',
        'diaphoresis',
        'easy arousal',
        'uncooperativeness',
    ]
    GENERAL_ABNORMAL_LIST2 = ['cachetic appearance']
    GENERAL_ABNORMAL_LIST3 = [
        'malnourished appearance',
        'underweight',
        'overweight',
        'obese',
        'morbidly obese',
    ]
    GENERAL_NORMAL_LIST = ['well appearing', 'well developed', 'well nourished']

    HEAD_AND_FACE_ABNORMAL_LIST1 = ['macrocephaly', 'microcephaly']
    HEAD_AND_FACE_ABNORMAL_LIST2 = [
        'laceration',
        'scars',
        'abrasion',
        'lesions',
        'masses',
        'raccoon eyes',
        'Battle’s sign contusion',
    ]
    HEAD_AND_FACE_NORMAL_LIST = ['normocephalic', 'atraumatic']

    EYES_ABNORMAL_LIST1 = [
        'uneven size',
        'uneven shape',
        'non-reactive to light',
        'non-reactive to accomodation',
    ]
    EYES_ABNORMAL_LIST2 = ['nystagmus', 'abnormal EOM']
    EYES_ABNORMAL_LIST3 = [
        'scleral icterus',
        'injection',
        'discharge',
        'chemosis',
        'exudate',
        'stye',
        'periorbital erythema',
    ]
    EYES_NORMAL_LIST = ['PERRL', 'EOM intact', 'conjunctiva clear']

    MOUTH_AND_THROAT_ABNORMAL_LIST1 = ['dry mucous membranes']
    MOUTH_AND_THROAT_ABNORMAL_LIST2 = [
        'post-nasal drainage',
        'exudate',
        'tonsillar hypertrophy',
        'tonsillar abscess',
        'pharyngeal swelling',
        'pharyngeal erythema',
        'uvula swelling',
        'gingival swelling',
        'tongue lesions',
        'tongue deviation',
        'palate mass',
        'palate lesions',
    ]
    MOUTH_AND_THROAT_ABNORMAL_LIST3 = ['lip lesions', 'cyanosis', 'pale']
    MOUTH_AND_THROAT_ABNORMAL_LIST4 = ['oral lesions', 'laceration', 'angioedema']
    MOUTH_AND_THROAT_ABNORMAL_LIST5 = [
        'poor dentition',
        'dental caries',
        'dental abscess',
        'dental tenderness',
        'dentures',
    ]
    MOUTH_AND_THROAT_ABNORMAL_LIST6 = [
        'tenderness with palpation of salivary gland',
        'enlargement',
        'induration',
        'abscess',
    ]
    MOUTH_AND_THROAT_NORMAL_LIST = [
        'moist mucous membranes',
        'oropharynx clear',
        'lips normal',
        'gums normal',
        'good dentition',
        'salivary glands normal',
    ]

    NECK_ABNORMAL_LIST1 = [
        'lymphadenopathy',
        'cervical adenopathy',
        'carotid bruit',
        'crepitus',
        'firmness',
        'tracheal deviation',
        'JVD',
        'hepatojugular reflux',
        'tracheostomy',
    ]
    NECK_ABNORMAL_LIST2 = [
        'decreased ROM',
        'pain with movement',
        'torticollis',
        'Brudzinski\'s sign',
        'Kernig\'s sign',
        'nuchal rigidity',
    ]
    NECK_ABNORMAL_LIST3 = ['thyromegaly', 'thyroid tenderness', 'mass']
    NECK_NORMAL_LIST = ['supple', 'ROM normal', 'thyroid normal']

    RESPIRATORY_ABNORMAL_LIST1 = [
        'wheezes',
        'rhonchi',
        'rales',
        'crackles',
        'stridor',
        'decreased breath sounds',
        'distant lung sounds',
        'decreased air movement',
        'tachypnea',
        'bradypnea',
    ]
    RESPIRATORY_ABNORMAL_LIST2 = [
        'respiratory distress',
        'labored breathing',
        'accessory muscle usage',
        'intercostal retractions',
        'diaphragm movement',
    ]
    RESPIRATORY_ABNORMAL_LIST3 = ['tenderness to palpation']
    RESPIRATORY_NORMAL_LIST = [
        'clear to auscultation bilaterally',
        'respiratory effort normal',
        'non-tender',
    ]

    CARDIOVASCULAR_ABNORMAL_LIST1 = ['tachycardia', 'bradycardia']
    CARDIOVASCULAR_ABNORMAL_LIST2 = [
        'irregular rhythm',
        'regularly irregular',
        'irregularly irregular',
    ]
    CARDIOVASCULAR_ABNORMAL_LIST3 = [
        'murmur',
        'S1 murmur',
        'S2 murmur',
        'systolic murmur',
        'diastolic murmur',
        'friction rubs',
        'gallops',
    ]
    CARDIOVASCULAR_ABNORMAL_LIST4 = [
        'pitting edema',
        'lower extremity edema',
        'decreased peripheral pulse',
        'JVD',
        'carotid bruit',
        'displaced PMI',
    ]
    CARDIOVASCULAR_NORMAL_LIST = [
        'regular rate',
        'regular rhythm',
        'heart sounds normal',
        'peripheral pulses intact',
    ]

    GASTROINTESTIANL_ABNORMAL_LIST1 = [
        'hepatomegaly',
        'splenomegaly',
        'firm',
        'mass',
        'pulsatile mass',
    ]
    GASTROINTESTIANL_ABNORMAL_LIST2 = [
        'tenderness to palpation',
        'rebound',
        'guarding',
        'McBurney\'s sign',
        'Murphy\'s sign',
        'pressure',
        'Blumberg sign',
        'obturator sign',
        'pain elicited with deep palpation',
        'pain elicited with superficial palpation',
        'psoas sign',
        'Rovsing\'s sign',
    ]
    GASTROINTESTIANL_ABNORMAL_LIST3 = ['distention', 'shifting dullness', 'fluid wave']
    GASTROINTESTIANL_ABNORMAL_LIST4 = [
        'absent bowel sounds',
        'abdominal bruit',
        'borborygmi',
        'hyperactive bowel sounds',
        'hypoactive bowel sounds',
        'tinkling sounds',
    ]
    GASTROINTESTIANL_ABNORMAL_LIST5 = [
        'hernia',
        'scars',
        'injury',
        'contoured abdomen',
        'Cullen\'s sign',
        'femoral hernia',
        'flat abdomen',
        'Grey Turner\'s sign',
        'inguinal hernia',
        'protuberant abdomen',
        'striae',
        'umbilical hernia',
        'ventral wall hernia',
        'round abdomen',
    ]
    GASTROINTESTIANL_NORMAL_LIST = [
        'soft',
        'nontender',
        'nondistended',
        'bowel sounds normal',
        'appearance normal',
    ]

    SKIN_ABNORMAL_LIST1 = ['cool']
    SKIN_ABNORMAL_LIST2 = [
        'moist',
        'dry',
        'diaphoresis',
        'induration',
        'tightening',
        'subcutaneous nodules',
    ]
    SKIN_ABNORMAL_LIST3 = [
        'rash',
        'lesion',
        'laceration',
        'ecchymosis',
        'edema',
        'abrasion',
        'wound',
        'scars',
        'burn',
        'acne',
        'petechiae',
        'ulcerations',
    ]
    SKIN_ABNORMAL_LIST4 = [
        'erythema',
        'pallor',
        'cyanosis',
        'jaundice',
        'ashen color',
        'sallow',
        'mottled',
    ]
    SKIN_ABNORMAL_LIST5 = [
        'clubbing',
        'cyanosis',
        'petechiae',
        'inflammation',
        'ischemia',
        'nodes',
    ]
    SKIN_NORMAL_LIST = [
        'warm',
        'well hydrated',
        'appearance normal',
        'color normal',
        'inspection of digits normal',
    ]

    MUSCULOSKELETAL_ABNORMAL_LIST1 = [
        'tenderness to palpation',
        'bony tenderness',
        'edema',
        'masses',
        'crepitus',
        'effusions',
        'asymmetry',
        'deformity',
    ]
    MUSCULOSKELETAL_ABNORMAL_LIST2 = [
        'pain with active ROM',
        'pain with passive ROM',
        'reduced active ROM',
        'reduced passive ROM',
    ]
    MUSCULOSKELETAL_ABNORMAL_LIST3 = ['dislocation', 'subluxation', 'laxity']
    MUSCULOSKELETAL_NORMAL_LIST = [
        'normal to palpation',
        'ROM normal',
        'stability normal',
    ]

    BACK_ABNORMAL_LIST1 = [
        'asymmetry',
        'curvature',
        'deformity',
        'edema',
        'spasm',
        'pain with active ROM',
        'midline tenderness',
        'CVA tenderness',
        'paraspinal tenderness',
        'step off',
    ]
    BACK_ABNORMAL_LIST2 = ['decreased ROM', 'positive straight leg test']
    BACK_NORMAL_LIST = ['appearance normal', 'ROM normal']

    NEUROLOGICAL_ABNORMAL_LIST1 = [
        'disoriented',
        'confused',
        'unresponsive',
        'lethargic',
        'impaired RAM',
    ]
    NEUROLOGICAL_ABNORMAL_LIST2 = [
        'cranial nerve deficit',
        'facial asymmetry',
        'dysarthria',
        'visual field deficit',
        'seizure activity',
    ]
    NEUROLOGICAL_ABNORMAL_LIST3 = ['abnormal gait', 'abnormal tandem walk']
    NEUROLOGICAL_ABNORMAL_LIST4 = [
        'asymmetrical reflexes',
        'abnormal deep tendon reflexes',
        'Babinski reflex',
    ]
    NEUROLOGICAL_ABNORMAL_LIST5 = [
        'weakness',
        'muscle atrophy',
        'abnormal movements',
        'spasm',
        'pronator drift',
        'flaccid',
        'cog wheel',
    ]
    NEUROLOGICAL_ABNORMAL_LIST6 = [
        'tremor',
        'abnormal finger to nose',
        'abnormal coordination',
        'abnormal heel to shin',
        'ataxia',
    ]
    NEUROLOGICAL_ABNORMAL_LIST7 = ['sensory deficit', 'Romberg positive']
    NEUROLOGICAL_NORMAL_LIST = [
        'alert and oriented x4',
        'cranial nerves II-XII grossly intact without focal changes',
        'gait normal',
        'reflexes normal',
        'normal strength and tone',
        'coordination normal',
        'sensation normal',
    ]

    PSYCHIATRIC_ABNORMAL_LIST1 = [
        'anxious mood',
        'depressed mood',
        'agitated',
        'hyperactive',
    ]
    PSYCHIATRIC_ABNORMAL_LIST2 = [
        'impaired memory',
        'impaired recent memory',
        'impaired remote memory',
    ]
    PSYCHIATRIC_ABNORMAL_LIST3 = [
        'flat affect',
        'labile affect',
        'blunt affect',
        'angry affect',
        'tearful affect',
    ]
    PSYCHIATRIC_ABNORMAL_LIST4 = [
        'suicidal ideation',
        'plan of suicide',
        'homicidal ideation',
        'plan of homicide',
        'impulsive judgment',
        'inappropriate judgment',
        'impaired cognition',
    ]
    PSYCHIATRIC_NORMAL_LIST = [
        'mood normal',
        'memory normal',
        'affect normal',
        'judgment normal',
    ]

    BREASTS_ABNORMAL_LIST1 = [
        'bleeding',
        'nipple discharge',
        'asymmetry',
        'swelling',
        'inverted nipple',
        'skin change',
    ]
    BREASTS_ABNORMAL_LIST2 = [
        'tenderness',
        'masses',
        'axillary adenopathy',
        'supraclavicular adenopathy',
        'pectoral adenopathy',
    ]
    BREASTS_NORMAL_LIST = ['normal on inspection', 'no findings with palpation']

    GENITOURINARY_FEMALE_ABNORMAL_LIST1 = [
        'discharge',
        'vaginal bleeding',
        'lesions',
        'swelling',
        'erythema',
        'excoriations',
        'prolasped vagina',
    ]
    GENITOURINARY_FEMALE_ABNORMAL_LIST2 = [
        'cervical motion tenderness',
        'cervical lesion',
    ]
    GENITOURINARY_FEMALE_ABNORMAL_LIST3 = [
        'bleeding',
        'deviated uterus',
        'enlarged uterus',
        'prolapsed uterus',
    ]
    GENITOURINARY_FEMALE_ABNORMAL_LIST4 = [
        'urethal scarring',
        'urethral mass',
        'urethral tenderness',
        'prolapsed urethra',
    ]
    GENITOURINARY_FEMALE_ABNORMAL_LIST5 = [
        'bladder fullness',
        'bladder mass',
        'bladder tenderness',
    ]
    GENITOURINARY_FEMALE_ABNORMAL_LIST6 = ['adnexal mass', 'adnexal fullness']
    GENITOURINARY_FEMALE_NORMAL_LIST = [
        'external genitalia normal',
        'cervix normal',
        'uterus normal',
        'urethra normal',
        'bladder normal',
        'adnexa normal',
    ]

    GENITOURINARY_MALE_ABNORMAL_LIST1 = [
        'discharge',
        'rash',
        'penile tenderness',
        'lesions',
        'swelling',
        'erythema',
        'phimosis',
        'paraphimosis',
        'hypospadias',
    ]
    GENITOURINARY_MALE_ABNORMAL_LIST2 = [
        'tenderness',
        'epididymis inflammation',
        'enlarged epididymis',
        'cremasteric reflex absent',
        'hydrocele',
        'varicocele',
        'inguinal hernia',
        'inguinal adenopathy',
        'testicular mass',
    ]
    GENITOURINARY_MALE_ABNORMAL_LIST3 = ['undescended testicle']
    GENITOURINARY_MALE_NORMAL_LIST = [
        'normal (un)circumcised male',
        'testes normal',
        'testes descended bilaterally',
    ]

    RECTAL_ABNORMAL_LIST1 = [
        'external hemorrhoid',
        'internal hemorrhoid',
        'anal fissure',
        'abnormal sphincter tone',
        'rectal mass',
    ]
    RECTAL_ABNORMAL_LIST2 = [
        'prostate enlargement',
        'prostate tenderness',
        'prostate nodule',
        'mass',
    ]
    RECTAL_ABNORMAL_LIST3 = ['guaiac positive']
    RECTAL_NORMAL_LIST = ['sphincter tone normal', 'prostate normal', 'guaiac negative']

    def click_on_pe_tab(self):
        self.wait_for_visibility_of(self.PE_TAB)
        self.click_and_wait(self.PE_TAB, 1)

    def expand_blocks_by_text(self, text):
        block_header_locator = (
            By.XPATH,
            f'//app-nb-pe-group//section//div[@class=\'nbblock__item__header__hl\' and text()=\'{text}\']',
        )
        parent_locator = (
            By.XPATH,
            f'//app-nb-pe-group//section//div[@class=\'nbblock__item__header__hl\' and text()=\'{text}\']/parent::*/parent::*/parent::*/parent::*',
        )
        block_header_element = self.get_element(block_header_locator, 10)
        if 'nbblock--collapsed' in self.get_attribute(parent_locator, 'class'):
            block_header_element.click()
            print('block expaned.')
        else:
            print('block already expanded.')

    def collapse_blocks_by_text(self, text):
        block_header_locator = (
            By.XPATH,
            f'//app-nb-pe-group//section//div[@class=\'nbblock__item__header__hl\' and text()=\'{text}\']',
        )
        parent_locator = (
            By.XPATH,
            f'//app-nb-pe-group//section//div[@class=\'nbblock__item__header__hl\' and text()=\'{text}\']/parent::*/parent::*/parent::*/parent::*',
        )
        block_header_element = self.get_element(block_header_locator, 10)
        if 'nbblock--collapsed' not in self.get_attribute(parent_locator, 'class'):
            block_header_element.click()
            print('block collapsed.')
            print(self.get_attribute(parent_locator, 'class'))
        else:
            print('block already collapsed.')

    def get_block_attribute_by_text(self, text):
        parent_locator = (
            By.XPATH,
            f'//app-nb-pe-group//section//div[@class=\'nbblock__item__header__hl\' and text()=\'{text}\']/parent::*/parent::*/parent::*/parent::*',
        )

        return self.get_attribute(parent_locator, 'class')

    def check_mark_block_by_index(self, index):
        block_check_box_locator = (
            By.XPATH,
            f'(//app-nb-pe-group//section//input)[{index}]',
        )
        block_check_box_element = self.get_element(block_check_box_locator, 5)
        block_check_box_element.click()

    def uncheck_mark_block_by_index(self, index):
        block_check_box_locator = (
            By.XPATH,
            f'(//app-nb-pe-group//section//input)[{index}]',
        )
        block_check_box_element = self.get_element(block_check_box_locator, 5)
        block_check_box_element.click()

    def check_section_class_by_index(self, index):
        block_check_box_locator = (By.XPATH, f'(//app-nb-pe-group//section)[{index}]')
        block_check_box_element = self.get_element(block_check_box_locator, 5)
        return block_check_box_element.get_attribute('class')

    def collapse_all_block(self):
        block_list = [
            'General',
            'Head and face',
            'Eyes',
            'Mouth and throat',
            'Neck',
            'Respiratory',
            'Cardiovascular',
            'Gastrointestinal',
            'Skin',
            'Musculoskeletal',
            'Back',
            'Neurological',
            'Psychiatric',
            'Breasts',
            'Genitourinary - female',
            'Genitourinary - male',
            'Rectal',
        ]
        for block_name in block_list:
            self.collapse_blocks_by_text(block_name)

    def retry_get_text_from_list_of_elements(self, list_locator, attempt=5):
        tried = 0
        while tried < attempt:
            try:
                return self.get_list_of_text_from_elements(
                    self.get_elements(list_locator)
                )
            except StaleElementReferenceException:
                print('Exception in retry get text')

            tried += 1

    def get_random_index_of_descriptor(self, descriptor_list_locator):
        total_count = self.get_total_count(descriptor_list_locator)
        if total_count < 1:
            raise IndexError('Not enough data.')
        return random.randrange(total_count)

    def retry_click(self, list_locator, element_index, attempt=5):
        tried = 0
        while tried < attempt:
            try:
                return self.click_list_elements_by_index(list_locator, element_index)
            except StaleElementReferenceException:
                print('Exception in retry click element')

            tried += 1

    def click_list_elements_by_index(self, list_locator, index):
        self.get_elements(list_locator, 3)[index].click()

    def select_random_descriptor_for_custom_pe_preset(self):
        self.expand_blocks_by_text('General')
        # build_tab = BuildTab(self.driver)
        normal_index = self.get_random_index_of_descriptor(self.NORMAL_LIST_LOCATOR)
        self.retry_click(self.NORMAL_LIST_LOCATOR, normal_index)

        abnormal1_index = self.get_random_index_of_descriptor(
            self.ABNORMAL_LIST1_LOCATOR
        )
        self.retry_click(self.ABNORMAL_LIST1_LOCATOR, abnormal1_index)

        abnormal2_index = self.get_random_index_of_descriptor(
            self.ABNORMAL_LIST2_LOCATOR
        )
        self.retry_click(self.ABNORMAL_LIST2_LOCATOR, abnormal2_index)

        abnormal3_index = self.get_random_index_of_descriptor(
            self.ABNORMAL_LIST3_LOCATOR
        )
        self.retry_click(self.ABNORMAL_LIST3_LOCATOR, abnormal3_index)
        self.retry_click(self.ABNORMAL_LIST3_LOCATOR, abnormal3_index)

        self.collapse_blocks_by_text('General')

    def check_all_inputs(self, expected_value=True):
        input_elements = self.get_elements(self.PE_INPUT_LOCATOR)
        attribute_list = [
            input_element.get_attribute('checked') == 'true'
            for input_element in input_elements
        ]
        return all(attribute == expected_value for attribute in attribute_list)

    def check_no_inputs_checked(self):
        return self.check_all_inputs(expected_value=False)
