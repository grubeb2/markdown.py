'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual( 
                run_markdown('this line has no special handling'), 
                '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual( 
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')

    def test_blockquotes(self):
        self.assertEqual(run_markdown('> this should have blockquote tags'), 
                        '<p><blockquote>this should have blockquote tags</blockquote></p>')

    def test_h3(self):
        self.assertEqual(run_markdown('### this should have h3 tags'), 
                        '<p><h3>this should have h3 tags</h3></p>')

    def test_h2(self):
        self.assertEqual(run_markdown('## this should have h2 tags'), 
                        '<p><h2>this should have h2 tags</h2></p>')

    def test_h1(self):
        self.assertEqual(run_markdown('# this should have h1 tags'), 
                        '<p><h1>this should have h1 tags</h1></p>')

if __name__ == '__main__':
    unittest.main()

