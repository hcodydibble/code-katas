"""Grasshopper - Terminal game combat function - Return remaining health after
taking damage.

# 1 Best Practices solution by ZozoFouchtra and others

def combat(health, damage):
    return max(0, health-damage)
"""


def combat(health, damage):
    """Find remaining health after taking damage."""
    return 0 if health - damage < 0 else health - damage
