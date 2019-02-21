import numpy as np
from .allegiance import allegiance


def integration(temporalcommunities, staticcommunities):
    """
    Calculates the integration coefficient for each node. Measures the average probability
    that a node is in the same community as nodes from other systems.

      Parameters:
      ------------
      temporalcommunities :  array
          temporal communities vector (node,time)
      staticcommunities : array
          Static communities vector for each node

      Returns:
      -------
      Icoeff : array
          integration coefficient for each node

    References:
    ----------
    Danielle S. Bassett, Muzhi Yang, Nicholas F. Wymbs, Scott T. Grafton.
    Learning-Induced Autonomy of Sensorimotor Systems. Nat Neurosci. 2015 May;18(5):744-51.

    Marcelo Mattar, Michael W. Cole, Sharon Thompson-Schill, Danielle S. Bassett.
    A Functional Cartography of Cognitive Systems. PLoS Comput Biol. 2015 Dec
    2;11(12):e1004533.
    """

    # make sure the static and temporal communities have the same number of nodes
    if staticcommunities.shape[0] != temporalcommunities.shape[0]:
        raise ValueError(
            'Temporal and static communities have different dimensions')

    alleg = allegiance(temporalcommunities)

    Icoeff = np.zeros(len(staticcommunities))

    # calc integration for each node
    for i, statcom in enumerate(len(staticcommunities)):
        Icoeff[i] = np.mean(alleg[i, staticcommunities != statcom])

    return Icoeff
