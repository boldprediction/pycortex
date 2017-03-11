"""
==============
make animation
==============
The dynamic viewer generated by cortex can be used to make an animation 
such as a transition between inflated and flattened brain or a rotating 
brain, of a cortical surface. We show here an example.

"""

import cortex

# gather data Volume
volume = cortex.Volume.random(subject='S1', xfmname='fullhead')

# select path for the animated movie on disk
animation_path = '/path/to/save/animation'

# create viewer (additional viewer parameters can be specified here,
# such as omitting ROI labels for example)
handle = cortex.webgl.show(data=volume)

# Called after a call of the form: js_handle = cortex.webgl.show(DataViewObject)
# Start with left hemisphere view
start_view = dict(azimuth=90, altitude=90.5)

# utility functions to set the different views
prefix = dict(altitude='camera.', azimuth='camera.',
              pivot='surface.{subject}.', radius='camera.',
              unfold='surface.{subject}.')
_tolists = lambda p: {prefix[k]+k:[v] for k,v in p.items()}

handle._set_view(**_tolists(start_view))

# Initialize list
animation = []
# Append 5 key frames for a simple rotation
for az, idx in zip([90, 180, 270, 360, 450], [0, .5, 1.0, 1.5, 2.0]):
    animation.append({'state':'camera.azimuth', 'idx':idx, 'value':[az]})
# Animate! (use default settings)
handle.makeMovie(animation, filename=os.path.join(movie_path,'brainmovie%07d.png'))

# the 'movie_path' directory will now have all the frames of the animation