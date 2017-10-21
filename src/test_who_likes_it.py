"""Test function for who_likes_it module."""

import pytest

TEST_DATA = [([], "no one likes this"),
             (["Peter"], "Peter likes this"),
             (["Jacob", "Alex"], "Jacob and Alex like this"),
             (["Max", "John", "Mark"], "Max, John and Mark like this"),
             (["Alex", "Jacob", "Mark", "Max"], "Alex, Jacob and 2 others like this"),
             (['Ryan', 'Jonathon', 'Alexandra', 'Jeffery', 'Elizabeth', 'Gina',
               'Kristina', 'Hannah', 'Crystal', 'Patrick', 'Brandon', 'Daniel',
               'Christian'], "Ryan, Jonathon and 11 others like this"),
             (['Ernest', 'Stephanie'], "Ernest and Stephanie like this"),
             (['Angelica', 'Karen', 'Kevin', 'William', 'Michaela', 'Kelly',
               'Ashley', 'Maria', 'Edward', 'Gregory', 'Sarah', 'Robert',
               'Sergio', 'Marvin', 'Nicole', 'Jeremy', 'Charles', 'Sandra',
               'Cindy', 'Thomas', 'Dan', 'Karla', 'Travis', 'Pamela',
               'Kimberly', 'Robert', 'James', 'David', 'Geoffrey', 'Patrick',
               'Nicole', 'Mitchell', 'Angela', 'Kayla', 'Madeline', 'Joann',
               'Maria', 'Ryan', 'Michelle', 'William', 'Johnny', 'Michael',
               'Patricia'], "Angelica, Karen and 41 others like this"),
             (['Lisa', 'Katrina', 'Kelly', 'Kyle', 'Catherine', 'Kimberly',
               'Mason', 'Diana', 'Samantha', 'Kimberly', 'Sherry', 'Joseph',
               'Allison', 'Mark', 'Virginia', 'Christopher', 'Manuel',
               'Michelle', 'Adam', 'Brenda', 'Bradley', 'Marissa', 'Carmen',
               'Carol', 'Kathleen', 'Brandon', 'Richard', 'Tara', 'Bonnie',
               'Richard', 'Bianca', 'Donald', 'Jonathan', 'Amanda', 'Jennifer',
               'Veronica', 'Alison', 'Diane', 'Olivia', 'Joe', 'Janet',
               'Stephanie', 'Scott', 'Dale', 'Natasha', 'Stephen', 'Laura',
               'Brian', 'Lynn', 'Kurt', 'Julia', 'Janet', 'Cory', 'Cody',
               'Mark', 'Elizabeth', 'Leslie', 'Bruce', 'Cindy', 'William',
               'Devin', 'Michael', 'Paul', 'Lindsey', 'Julie', 'Michelle',
               'Carla', 'Ian', 'Dennis', 'Lindsay', 'Rose', 'Emily', 'Jessica',
               'Jerry', 'Riley', 'Jeffery', 'Steven', 'Alisha', 'Mark',
               'Joseph', 'Andrew', 'Joshua', 'Nathan'], "Lisa, Katrina and 81 others like this")]


@pytest.mark.parametrize("string, result", TEST_DATA)
def test_likes(string, result):
    """Test for likes function."""
    from who_likes_it import likes
    assert likes(string) == result
