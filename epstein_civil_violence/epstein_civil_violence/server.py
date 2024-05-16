import mesa

from .agent import Citizen, Cop
from .model import EpsteinCivilViolence
from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.UserParam import Choice

COP_COLOR = "#000000"
AGENT_QUIET_COLOR = "#648FFF"
AGENT_REBEL_COLOR = "#FE6100"
JAIL_COLOR = "#808080"
JAIL_SHAPE = "rect"


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "circle",
        "x": agent.pos[0],
        "y": agent.pos[1],
        "Filled": "true",
    }

    if type(agent) is Citizen:
        color = (
            AGENT_QUIET_COLOR if agent.condition == "Quiescent" else AGENT_REBEL_COLOR
        )
        color = JAIL_COLOR if agent.jail_sentence else color
        shape = JAIL_SHAPE if agent.jail_sentence else "circle"
        portrayal["Color"] = color
        portrayal["Shape"] = shape
        if shape == "rect":
            portrayal["w"] = 0.9
            portrayal["h"] = 0.9
        else:
            portrayal["r"] = 0.5
            portrayal["Filled"] = "false"
        portrayal["Layer"] = 0

    elif type(agent) is Cop:
        portrayal["Color"] = COP_COLOR
        portrayal["r"] = 0.9
        portrayal["Layer"] = 1

    return portrayal

updating_scheme_param = Choice(
    "Updating Scheme",
    choices=["RandomActivation", "SimultaneousActivation", "StagedActivation", "BaseScheduler"],
    value="RandomActivation"
)

#### Government Legitimacy distributions and parameters

legitimacy_dist_param = Choice(
    "Legitimacy Distribution",
    choices=["uniform", "normal", "gamma"],
    value="uniform"
)

#legitimacy_param_uniform = mesa.visualization.Slider("Uniform Min-Max", 0.0, 0.0, 1.0, 0.05)
legitimacy_param_normal_mean = mesa.visualization.Slider("Normal Mean", 0.5, 0.0, 1.0, 0.05)
legitimacy_param_normal_stddev = mesa.visualization.Slider("Normal StdDev", 0.1, 0.01, 0.5, 0.01)
gamma_shape = mesa.visualization.Slider("Gamma Shape", 2, 0.5, 5.0, 0.1)
gamma_scale = mesa.visualization.Slider("Gamma Scale", 2, 0.5, 5.0, 0.1)


model_params = {
    "height": 40,
    "width": 40,
    "citizen_density": mesa.visualization.Slider(
        "Initial Agent Density", 0.7, 0.0, 0.9, 0.1
    ),
    "cop_density": mesa.visualization.Slider(
        "Initial Cop Density", 0.04, 0.0, 0.1, 0.01
    ),
    "citizen_vision": mesa.visualization.Slider("Citizen Vision", 7, 1, 10, 1),
    "cop_vision": mesa.visualization.Slider("Cop Vision", 7, 1, 10, 1),
    # "legitimacy": mesa.visualization.Slider(
    #     "Government Legitimacy", 0.82, 0.0, 1, 0.01
    # ),
    "legitimacy_distribution": legitimacy_dist_param, ### This is new
    # "legitimacy_param_uniform": legitimacy_param_uniform,
    "legitimacy_param_normal_mean": legitimacy_param_normal_mean,
    "legitimacy_param_normal_stddev": legitimacy_param_normal_stddev,
    "legitimacy_param_gamma_shape": gamma_shape,
    "legitimacy_param_gamma_scale": gamma_scale,  #### This is new
    "max_jail_term": mesa.visualization.Slider("Max Jail Term", 30, 0, 50, 1),
    "updating_scheme": updating_scheme_param
}
# canvas_element = mesa.visualization.CanvasGrid(citizen_cop_portrayal, 40, 40, 480, 480)
canvas_element = CanvasHexGrid(citizen_cop_portrayal, 40, 40, 480, 480)
chart = mesa.visualization.ChartModule(
    [
        {"Label": "Quiescent", "Color": "#648FFF"},
        {"Label": "Active", "Color": "#FE6100"},
        {"Label": "Jailed", "Color": "#808080"},
    ],
    data_collector_name="datacollector",
)


server = mesa.visualization.ModularServer(
    EpsteinCivilViolence,
    [canvas_element, chart],
    "Epstein Civil Violence",
    model_params
)