from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.tokenize import word_tokenize
from utils.logger import logger
from typing import List, Union

class BLEUEvaluator:
    def __init__(self):
        self.smoothing = SmoothingFunction().method1

    def evaluate(self, reference_sentences: Union[str, List[str]], 
                 hypothesis_sentences: Union[str, List[str]], 
                 source_sentences: Union[str, List[str]] = None) -> float:
        try:
            reference_sentences = [reference_sentences] if isinstance(reference_sentences, str) else reference_sentences
            hypothesis_sentences = [hypothesis_sentences] if isinstance(hypothesis_sentences, str) else hypothesis_sentences

            if not reference_sentences or not hypothesis_sentences:
                logger.warning("Empty input: reference or hypothesis sentences are empty.")
                return 0.0

            total_bleu = 0.0
            num_sentences = len(hypothesis_sentences)

            for ref, hyp in zip(reference_sentences, hypothesis_sentences):
                ref_tokens = word_tokenize(ref.lower())
                hyp_tokens = word_tokenize(hyp.lower())
                
                # Use sentence_bleu with smoothing
                bleu_score = sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=self.smoothing)
                total_bleu += bleu_score

            average_bleu = total_bleu / num_sentences
            return average_bleu

        except Exception as e:
            logger.error(f"An error occurred while calculating BLEU score: {str(e)}")
            return 0.0
    
    async def evaluate_async(self, reference_sentences: Union[str, List[str]], 
                            hypothesis_sentences: Union[str, List[str]], 
                            source_sentences: Union[str, List[str]] = None) -> float:
        return self.evaluate(reference_sentences, hypothesis_sentences, source_sentences)