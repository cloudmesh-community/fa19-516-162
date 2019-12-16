import oci
from cloudmesh.configuration.Config import Config
from cloudmesh.oracle.storage.Provider import Provider as StorageProvider

# Initialize
config_file = "~/.cloudmesh/cloudmesh.yaml"
config = Config(config_file)["cloudmesh"]["cloud"]["oracle"]["credentials"]
compute = oci.core.ComputeClient(config)
storage_provider = StorageProvider('oracle')

# Download File
result = storage_provider.get(r"big-data\mnist-deep-learning.py",
                              r"mnist-deep-learning2.py")

print("MNIST Deep Learning Code Downloaded")

# Run File
exec(open("mnist-deep-learning.py").read())
