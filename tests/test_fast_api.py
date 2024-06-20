import unittest
from api_service.fast_api_demo import complex_math_operation, math_operation  # Replace with your actual function
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestAddition(unittest.TestCase):

    def test_complex_math_operation_api(self):
        result = complex_math_operation(3, 4)
        logger.info("************")
        logger.info(result)
        logger.info("************")

    def test_complex_math_operation(self):
        result = math_operation(3, 4)
        logger.info("************")
        logger.info(result)
        logger.info("************")