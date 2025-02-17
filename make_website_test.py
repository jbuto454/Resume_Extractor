import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )

    def test_read_and_store_file(self):

        #test the first resume
        self.assertEqual(
            list,
            type(read_and_store_file('resume.txt'))
        )

        #test the second resume
        self.assertEqual(
            list,
            type(read_and_store_file('TestResumes/resume_bad_name_lowercase/resume.txt'))
        )

        #test the third resume
        self.assertEqual(
            list,
            type(read_and_store_file('TestResumes/resume_courses_w_whitespace/resume.txt'))
        )

        #test the fourth resume
        self.assertEqual(
            list,
            type(read_and_store_file('TestResumes/resume_courses_weird_punc/resume.txt'))
        )

        #test the fifth resume
        self.assertEqual(
            list,
            type(read_and_store_file('TestResumes/resume_projects_w_whitespace/resume.txt'))
        )

        #test the sixth resume
        self.assertEqual(
            list,
            type(read_and_store_file('TestResumes/resume_projects_with_blanks/resume.txt'))
        )

        #test the seventh resume
        self.assertEqual(
            list,
            type(read_and_store_file('TestResumes/resume_template_email_w_whitespace/resume.txt'))
        )

        #test the eighth resume
        self.assertEqual(
            list,
            type(read_and_store_file('TestResumes/resume_wrong_email/resume.txt'))
        )


    def test_detect_and_return_name(self):

        #test an expected name format
        self.assertEqual(
            'Brandon',
            detect_and_return_name(['Brandon'])
        )

        #test an invalid name format
        self.assertEqual(
            'Invalid Name',
            detect_and_return_name(['brandon'])
        )


    def test_detect_and_return_email(self):

        #test an expected email format with the email second in the list
        self.assertEqual(
            'jakebuto@pm.edu',
            detect_and_return_email(['Jake','jakebuto@pm.edu'])
        )

        #test an expected email format with the email first in the list
        self.assertEqual(
            'jakebuto@pm.edu',
            detect_and_return_email(['jakebuto@pm.edu', 'Jake'])
        )

        #test an expected email format with the email second in the list
        self.assertEqual(
            'jakebuto@pm.com',
            detect_and_return_email(['Jake','jakebuto@pm.com'])
        )

        #test an expected email format with the email first in the list
        self.assertEqual(
            'jakebuto@pm.com',
            detect_and_return_email(['jakebuto@pm.com', 'Jake'])
        )

        #test an unexpected email format with the email second in the list
        self.assertEqual(
            '',
            detect_and_return_email(['Jake','jakebuto@pm.me'])
        )

        #test an unexpected email format with the email first in the list
        self.assertEqual(
            '',
            detect_and_return_email(['jakebuto@pm.me', 'Jake'])
        )

        #test an unexpected email format with the email second in the list
        self.assertEqual(
            '',
            detect_and_return_email(['Jake','jakebuto4@pm.me'])
        )

        #test an unexpected email format with the email first in the list
        self.assertEqual(
            '',
            detect_and_return_email(['jakebuto4@pm.me', 'Jake'])
        )

    def test_detect_and_return_courses(self):

        #test the course list second in the list
        self.assertEqual(
            list,
            type(detect_and_return_courses(['Courses, something, something something, something', 'something something something']))
        )

        #test the course list first in the list
        self.assertEqual(
            list,
            type(detect_and_return_courses(['something something something, something', 'Courses, something, something, something']))
        )

        #test a non-valid course list
        with self.assertRaises(TypeError):
            detect_and_return_courses(['blah'])


    def test_detect_and_return_projects(self):

        #test project list with the correct amount of '-' signs at the end of the project list
        self.assertEqual(
            ['Projects','something','something'],
            detect_and_return_projects(['Projects','something','something','---------------'])
        )

        #test project list with the wrong amount of '-' signs at the end of the project list
        with self.assertRaises(UnboundLocalError):
            detect_and_return_projects(['Projects','something','something','-----'])

        #test project list with no word 'Projects' at thge start of the list
        with self.assertRaises(ValueError):
            detect_and_return_projects(['','something','something','-----------------'])

        #test project list with no projects
        self.assertEqual(
            ['Projects'],
            detect_and_return_projects(['Projects','---------------'])
        )


    def test_read_html_file_to_list(self):

        #test project list with the correct amount of '-' signs at the end of the project list
        self.assertEqual(
            list,
            type(read_html_file_to_list('resume.txt'))
        )


if __name__ == '__main__':
    unittest.main()