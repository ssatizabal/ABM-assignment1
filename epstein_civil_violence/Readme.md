# Epstein Civil Violence Model

## Summary

How do variations in regime legitimacy, policing capacity, and external interventions influence the dynamics of civil unrest and citizen compliance? I try to partly answer this research question by proposing an Agent-Based model as an adjusted version of Joshua Epstein's simulation of how civil unrest grows and is suppressed (Epstein, 2002). The original paper presents a model in which a central authority seeks to suppress decentralized rebellion.  Some of the parameters of the original model include factors that affect the Citizens’ decision to rebel: hardship level, regime legitimacy, their perceived probability of arrest and jailed term. Within this model, some parameters have been identified to greatly affect the dynamics of rebellion (outcome) such as the function used to determine the arrest probability or the "maximum jail term" both highly alter the perception of risk of the agents and the results of rebellion. This is backed by theoretical and simulation evidence and provides a convincing argument for the model’s utility in understanding social conflicts (Lemos, 2017). 
Nonetheless, the model also has clear explanatory limitations such as the fact that hardships are uniform across agents instead of a relative deprivation (RD) and that legitimacy is uniform and constant in time instead of a dynamic, endogenous factor in which the structure of relationships significantly influences the likelihood and magnitude of rebellions (Lemos, 2017). 
Against this background, from Epstein’s model as a starting point, I implement three main changes following Wilensky (2004) and Lemos (2017). First, I allow the model to have an initial government legitimacy distribution instead of a constant value and allow for it to update for each agent increasing proportionally with the number of nearby jailed agents. This change partially follows Sussane Lohmann’s  (2008) concept of collective action cascades in which the regime legitimacy is not uniform across agents (citizens) but is rather a spectrum from extremist agents willing to change the status quo, to apathetic moderates and status quo supporters. Second, hardships and agent’s grievance – that are unique values for each agent -   are also updated and influenced by the value of other nearby agents. Third, I add an international aid shock following the frequency with which such aid has been given to regimes struggling with civil unrest.


## How to Run

To run the model interactively, run ``run.py`` in this directory. e.g.

```
    $ python3 run.py
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

## Files

* ``agent.py``: Core agent code.
* ``model.py``: Core model code.
* ``server.py``: Sets up the interactive visualization.
* ``Epstein Civil Violence.ipynb``: Jupyter notebook conducting some preliminary analysis of the model.


