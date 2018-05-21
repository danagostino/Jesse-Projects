import Warrior from './Warrior';

describe('Warrior', () => {
  test("appears as '@' on map", () => {
    expect(Warrior.character).toBe('@');
  });

  test('has 20 max health', () => {
    expect(Warrior.maxHealth).toBe(20);
  });
});
