
# Try to use multiprocessing module to process multiple keypoints simulataneously.
# (copy all required data serially to a buffer first to prevent data access races!)


# Ignore Ctypes interface for now, just re-implement C++ code in Python to start.


import rktracker

#import rktracker.trackers



class RKTracker(object):

    def __init__(self, search_window_size, match_area_size, tracker_func):
        #self._point_list = []
        #self._window_size = search_window_size
        #self._match_size = match_area_size


        # Function that takes this RKTracker instance and updates trackpoints.
        #self._tracker_func = tracker_func

        # These will be OpenCV Mat objects
        #self._last_frame = None
        #self._curr_frame = None


        pass


    def add_trackpoint(self, x, y):
        #self._point_list.append((x,y))
        pass


    def remove_trackpoint(self, x, y):
        pass


    def update_tracker(self, img_mat):
        # store img and call self._tracker_func(self)
        self._curr_frame = img;


        pass






def main():



    # Work out loop logistics first (also using cv2/SDL2)



    # Initialize rktracker and select tracker to use.

    #tracker = rktracker.trackers.Tracker_Python();








    pass



