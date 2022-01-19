from nn_adapt import *
import argparse
import importlib
import numpy as np
import os


# Parse for test case and number of refinements
parser = argparse.ArgumentParser()
parser.add_argument('model', help='The model')
parser.add_argument('test_case', help='The configuration file number')
parser.add_argument('-num_refinements', help='Number of mesh refinements')
parsed_args = parser.parse_args()
model = parsed_args.model
assert model in ['stokes', 'turbine']
test_case = int(parsed_args.test_case)
assert test_case in list(range(12))
num_refinements = int(parsed_args.num_refinements or 5)
assert num_refinements >= 0

# Setup
setup = importlib.import_module(f'{model}.config{test_case}')
field = setup.fields[0]
mesh = Mesh(f'{os.path.abspath(os.path.dirname(__file__))}/{model}/meshes/{test_case}.msh')
mh = MeshHierarchy(mesh, num_refinements)

# Run uniform refinement
qois = []
dofs = []
elements = []
print(f'Test case {test_case}')
for i, mesh in enumerate(mh):
    print(f'  Mesh {i}')
    print(f'    Element count        = {mesh.num_cells()}')
    fwd_sol = get_solutions(mesh, setup, solve_adjoint=False)
    fs = fwd_sol.function_space()
    J = assemble(setup.get_qoi(mesh)(fwd_sol))
    print(f'    Quantity of Interest = {J}')
    qois.append(qoi)
    dofs.append(sum(fs.dof_count))
    elements.append(mesh.num_cells())
    np.save(f'{model}/data/qois_uniform_{test_case}', qois)
    np.save(f'{model}/data/dofs_uniform_{test_case}', dofs)
    np.save(f'{model}/data/elements_uniform_{test_case}', elements)
