import os
import setuptools

# ref to https://github.com/pytorch/pytorch/blob/1b43883fd61a5e3525ea213262bfcb3aedc941d3/torch/utils/cpp_extension.py#L1740 for arch name
os.environ['TORCH_CUDA_ARCH_LIST'] = 'Pascal;Volta;Turing;Ampere'

from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ext_modules = [
    CUDAExtension(name='upfirdn2d.ops.upfirdn2d',
                  sources=['upfirdn2d/ops/upfirdn2d.cpp',
                           'upfirdn2d/ops/upfirdn2d_kernel.cu'],
                  headers=['upfirdn2d/ops/upfirdn2d.h'],
                  extra_compile_args={'nvcc': ['--use_fast_math']})
    ]

setuptools.setup(
    name='upfirdn2d',
    version='0.1',
    description='upfirdn2d',
    author='Minjun Li',
    url='https://github.com/minjunli/upfirdn2d',
    packages=setuptools.find_packages(),
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExtension},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
