"""Function to return information about the Forbes top 40."""
from data.forbes import billionaires


def richie_rich():
    oldest = None
    youngest = float('inf')
    for rich_guy in billionaires:
        if rich_guy['age'] < 80:
            if oldest is not None:
                if rich_guy['age'] > oldest['age']:
                    oldest = rich_guy
            else:
                oldest = rich_guy
        if youngest == float('inf'):
            youngest = rich_guy
        elif rich_guy['age'] < youngest['age'] and rich_guy['age'] > 0:
            youngest = rich_guy
    output = """
    Oldest Rich Dude under 80 is {}. He is {} years old and worth {}. His industry is {}.

    Youngest Rich Dude is {}. He is {} years old and worth {}. His industry is {}. 
    """.format(oldest['name'], oldest['age'], oldest['net_worth (USD)'], oldest['source'], youngest['name'], youngest['age'], youngest['net_worth (USD)'], youngest['source'])
    print(output)
    return oldest['name'], oldest['age'], oldest['net_worth (USD)'], oldest['source'], youngest['name'], youngest['age'], youngest['net_worth (USD)'], youngest['source']
