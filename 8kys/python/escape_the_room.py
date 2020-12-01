"""
https://www.codewars.com/kata/56a29b237e9e997ff2000048/train/python
Escape the room
You are creating an "Escape the room" game.
The first step is to create a hash table called rooms that contains all of the rooms of the game.
There should be at least 3 rooms inside it, each being a hash table with at least three properties
                                                                (e.g. name, description, completed).
"""

rooms = {}


@test.describe('room creation')
def example_tests():
    @test.it('should have at least three rooms')
    def example_test_case():
        test.expect(len(rooms) >= 3, 'Should have at least three rooms')

    @test.it('each room should be a dictionary')
    def example_test_case():
        for name in rooms.values():
            test.expect(isinstance(name, dict), f'{name} should be a dictionary')

    @test.it('should contain at least three properties per room')
    def example_test_case():
        for name in rooms.values():
            test.expect(len(name) >= 3, f'Not enough properties for room: {name}')