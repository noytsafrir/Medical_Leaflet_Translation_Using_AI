import unittest
import json, sys, os
from typing import Dict
from utils.logger import logger
from services.translation_manager import TranslationManager
from services.translation.testing_translation_handler import TestingTranslationHandler
from data.entities import EvaluationLeafletData
from data.boundaries import TranslationRequest

class TranslationAccuracyTest(unittest.TestCase):
    def setUp(self):
        self.testing_handler = TestingTranslationHandler()
        self.translation_manager = TranslationManager(self.testing_handler)
        self.translation_manager.initialize()
        with open('tests/test_data/leaflets/17-OPTALGIN.json', 'r', encoding='utf-8') as f:
            self.leaflet_data = json.load(f)

    def test_full_leaflet_translation(self):
        for section in self.leaflet_data['sections']:
            self.translate_and_evaluate_section(section)


    def translate_and_evaluate_section(self, section: Dict) -> float:
        for item in section['data']:
            if 'heb' in item and 'eng' in item and item['heb'] != "" and item['eng'] != "":
                translation_request = TranslationRequest(
                    source='he',
                    dest='en',
                    textInput=item['heb']
                )
                leaflet_data = EvaluationLeafletData(
                    leaflet_id=self.leaflet_data['dir_index'],
                    leaflet_name=self.leaflet_data['title'],
                    section_number=section['section_num'],
                    array_location=section['data'].index(item),
                    human_translation=item['eng']
                )
                translation_response = self.translation_manager.translate(
                    translation_request, 
                    evaluation_leaflet_data=leaflet_data
                ).translated_text

if __name__ == '__main__':
    unittest.main()


# import unittest
# import json, sys, os
# from typing import Dict
# from utils.logger import logger
# from services.evaluation.bleu_score import calculate_bleu
# from services.translation_manager import translation_manager
# from data.boundaries import TranslationRequest


# class TranslationAccuracyTest(unittest.TestCase):
#     def setUp(self):
#         translation_manager.initialize()
#         with open('tests/test_data/leaflets/Ursolit.json', 'r', encoding='utf-8') as f:
#             self.leaflet_data = json.load(f)

#     def test_full_leaflet_translation(self):
#         total_bleu_score = 0
#         total_sections = 0

#         for section in self.leaflet_data['sections']:
#             section_bleu_score = self.translate_and_evaluate_section(section)
#             if section_bleu_score is not None:
#                 total_bleu_score += section_bleu_score
#                 total_sections += 1

#         if total_sections > 0:
#             average_bleu_score = total_bleu_score / total_sections
#             self.assertGreaterEqual(average_bleu_score, 0.60, 
#                                     f"Average BLEU score {average_bleu_score} for the entire leaflet is below the threshold of 0.60")
#         else:
#             self.fail("No valid sections found for translation evaluation")

#     def translate_and_evaluate_section(self, section: Dict) -> float:
#         section_bleu_scores = []

#         for item in section['data']:
#             if 'heb' in item and 'eng' in item and item['heb'] != "" and item['eng'] != "":
#                 translation_request = TranslationRequest(
#                     source='he',
#                     dest='en',
#                     text_input=item['heb']
#                 )
#                 translation_response = translation_manager.translate(translation_request, human_verified_translation=item['eng']).translated_text
#                 if(translation_response != None and translation_response.strip() != ""):
#                     bleu_score = calculate_bleu(item['eng'], translation_response)
#                     section_bleu_scores.append(bleu_score)

#         if section_bleu_scores:
#             average_section_bleu = sum(section_bleu_scores) / len(section_bleu_scores)
#             logger.error(f"****************************************\n Section '{section['title']}' average BLEU score: {average_section_bleu} \n****************************************")
#             return average_section_bleu
#         else:
#             logger.error(f"~~~~~~~~~~ No valid items found in section '{section['title']}' for translation evaluation ~~~~~~~~~~")
#             return None

# if __name__ == '__main__':
#     unittest.main()