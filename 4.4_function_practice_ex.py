# first sayhello function uses positional arguments
def sayhello(name, greeting, punctuation):
    return(f'{greeting}, {name}{punctuation}')

# second sayhello function uses keyword arguments
def sayhello(name='friend', greeting='hello', punctuation='~'):
    return(f'{greeting}, {name}{punctuation}')

