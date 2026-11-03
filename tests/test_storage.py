import tempfile
import unittest
from pathlib import Path
from storage import ReplyStore, match_trigger, normalize_keyword, parse_color


class StorageTests(unittest.TestCase):
    def test_trigger_is_exact_and_case_insensitive(self):
        self.assertEqual(match_trigger('!!OFFLINE'), 'offline')
        self.assertEqual(match_trigger('  !!logsdump  '), 'logsdump')
        self.assertIsNone(match_trigger('!!offline please help'))
        self.assertIsNone(match_trigger('hello !!offline'))
        self.assertEqual(match_trigger('!!SUPPORT Furniture'), 'support furniture')
        self.assertEqual(match_trigger('!!support    furniture'), 'support furniture')
        self.assertEqual(match_trigger('!!support'), 'support')
        self.assertIsNone(match_trigger('!!support furniture please'))
        self.assertIsNone(match_trigger('!!support furniture extra'))
        self.assertIsNone(match_trigger('!!support\nfurniture'))

    def test_validating_names_and_colors(self):
        self.assertEqual(normalize_keyword('!!Logs'), 'logs')
        self.assertEqual(normalize_keyword('SUPPORT   Furniture'), 'support furniture')
        self.assertEqual(parse_color('#57F287'), 0x57F287)
        with self.assertRaises(ValueError):
            normalize_keyword('invalid keyword additional')
        with self.assertRaises(ValueError):
            parse_color('red')

    def test_persistence_is_per_guild(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'replies.sqlite3'
            db = ReplyStore(path)
            db.save(1, 'logs', '', 'Upload logs', 0x57F287)
            db.save(2, 'logs', 'Other', 'Different server', 0xAA00AA)
            db.save(1, 'bedrock', '', 'See wiki', 0x57F287)
            db.save(1, 'support', '', 'General support', 0x57F287)
            db.save(1, 'support furniture', '', 'Furniture help', 0x57F287)
            self.assertEqual(db.list(1), ['bedrock', 'logs', 'support', 'support furniture'])
            self.assertEqual(db.get(1, 'support furniture').body, 'Furniture help')
            self.assertEqual(db.get(2, 'logs').body, 'Different server')
            self.assertEqual(db.get(1, 'logs').body, 'Upload logs')
            db.close()
            reopened = ReplyStore(path)
            self.assertEqual(reopened.get(1, 'logs').body, 'Upload logs')
            self.assertEqual(reopened.get(1, 'support').body, 'General support')
            self.assertEqual(reopened.get(1, 'support furniture').body, 'Furniture help')
            self.assertTrue(reopened.delete(1, 'logs'))
            self.assertIsNone(reopened.get(1, 'logs'))
            self.assertEqual(reopened.get(2, 'logs').body, 'Different server')
            reopened.close()


if __name__ == '__main__':
    unittest.main()
