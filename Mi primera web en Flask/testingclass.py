import os
import helloworldflask
import unittest
import tempfile

class helloworldflaskTestCase(unittest.TestCase):
	# Aquí empieza el esqueleto principal
    def setUp(self):
        self.db_fd, helloworldflask.app.config['DATABASE'] = tempfile.mkstemp()
        helloworldflask.app.config['TESTING'] = True
        self.app = helloworldflask.app.test_client()
        helloworldflask.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(helloworldflask.app.config['DATABASE'])

	# Aquí acaba el esqueleto principal


    def test_empty(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data



if __name__ == '__main__':
    unittest.main()

