'''
Defines a class, Neuron473863510, of neurons from Allen Brain Institute's model 473863510

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473863510:
    def __init__(self, name="Neuron473863510", x=0, y=0, z=0):
        '''Instantiate Neuron473863510.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473863510_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Rorb-IRES2-Cre-D_Ai14_IVSCC_-168053.05.01.01_325404214_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473863510_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 35.64
            sec.e_pas = -85.0781555176
        for sec in self.apic:
            sec.cm = 2.19
            sec.g_pas = 2.11145615996e-06
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000914230933549
        for sec in self.dend:
            sec.cm = 2.19
            sec.g_pas = 3.82640431886e-06
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.000437884
            sec.gbar_Ih = 0.00199221
            sec.gbar_NaTs = 0.712822
            sec.gbar_Nap = 0.00124938
            sec.gbar_K_P = 0.0348364
            sec.gbar_K_T = 0.0166429
            sec.gbar_SK = 0.000249722
            sec.gbar_Kv3_1 = 0.280598
            sec.gbar_Ca_HVA = 0.00015339
            sec.gbar_Ca_LVA = 0.00334693
            sec.gamma_CaDynamics = 0.00402188
            sec.decay_CaDynamics = 991.141
            sec.g_pas = 0.000928657
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

