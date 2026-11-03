import unittest

from permissions import REPLY_EDITOR_ROLE_IDS, has_reply_editor_role


class ReplyEditorPermissionsTests(unittest.TestCase):
    def test_plugin_developer_is_allowed(self):
        self.assertTrue(has_reply_editor_role([1563858250456236032]))

    def test_contributor_is_allowed(self):
        self.assertTrue(has_reply_editor_role([1563864910285373502]))

    def test_unrelated_role_cannot_edit(self):
        self.assertFalse(has_reply_editor_role([1234567890]))

    def test_no_roles_cannot_edit(self):
        self.assertFalse(has_reply_editor_role([]))

    def test_member_with_multiple_roles_is_allowed(self):
        self.assertTrue(has_reply_editor_role([100, 1563864910285373502, 200]))

    def test_authorised_role_ids_are_exact(self):
        self.assertEqual(REPLY_EDITOR_ROLE_IDS, {
            1563858250456236032,
            1563864910285373502,
        })


if __name__ == "__main__":
    unittest.main()
