from phi import flow
flow.set_global_backend('torch')  # ✅ Activate PyTorch

from phi.torch.flow import *  # ✅ Should now work
print("phi.torch.flow is available ✅")
