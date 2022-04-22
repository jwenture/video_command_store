import os
import numpy as np
import pytorch

class StorageEngine():
    def __init__(self, storage_location, total_steps, video_shape, total_actions):
        self.storage_location = storage_location
        self.total_steps = total_steps
        self.video_shape = video_shape
        self.total_actions = total_actions

    def start_cycle(self):
        self.start_procedure()

    def start_procedure(self):
        raise NotImplementedError("This needs to be implemented separately")

    def end_cycle(self):
        self.end_procedure()

    def end_procedure(self):
        raise NotImplementedError("This needs to be implemented separately")

    def append_data(self):
        pass

    def append_procedure(self):
        raise NotImplementedError("This needs to be implemented separately")

    def retrieve_data(self):
        self.retrieve_procedure()

    def retrieve_procedure(self):
        raise NotImplementedError("This needs to be implemented separately")




class NumpyFolderStorageEngine(StorageEngine):
    """
    total_steps=200 an array of 200 rows will be created
    """
    def __init__(self, storage_location="./data",
                 total_steps=200,
                 video_shape=(480, 480, 3),
                 total_actions=3,
                 ):
        super().__init__(storage_location,total_steps, video_shape,total_actions)
        self.current_step = 0


    def start_procedure(self):
        self.data_store = np.zeros((self.total_steps, *self.video_shape))
        self.data_store += np.nan
        self.action_store = np.zeros((self.total_steps, self.total_actions))
        self.action_store += np.nan

    def end_procedure(self):
        pass

    def append_procedure(self,d a):
        self.data_store[self.current_step] = data
        self.action_store[self.current_step] = action

        self.current_step+=1

    def retrieve_procedure(self):
        pass


if __name__ == "__main__":
    main()