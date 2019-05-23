import unittest
import activedir

class TestActiveDir(unittest.TestCase):
    def test_find_user_in_group(self):
        parent = activedir.Group("parent")
        child = activedir.Group("child")
        sub_child = activedir.Group("sub_child")
        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)
        child.add_group(sub_child)
        parent.add_group(child)

        self.assertEqual(activedir.is_user_in_group("sub_child_user",sub_child),True)
        self.assertEqual(activedir.is_user_in_group("sub_child_user",parent),True)
        self.assertEqual(activedir.is_user_in_group("sub_child_user",child),True)
        self.assertEqual(activedir.is_user_in_group("sub_child_user1",child),False)
