##from tinytroupe import utils
##import tinytroupe

##lisa_ds = create_lisa_the_data_scientist()
##lisa_ds.listen_and_act("Tell me about your life")

from tinytroupe.examples import create_lisa_the_data_scientist

lisa = create_lisa_the_data_scientist() # instantiate a Lisa from the example builder
lisa.listen_and_act("Tell me about your life.")