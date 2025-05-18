import laspy
from qpoint3df import QPoint3DF

def load_laz_file(file_path, width, height):
    """
    Loads .laz LiDAR data using laspy and lazrs and rescales it for display.

    Args:
        file_path (str): Path to the .laz file
        width (int): Canvas width for scaling
        height (int): Canvas height for scaling

    Returns:
        List of QPoint3DF objects (scaled)
    """
    laz = laspy.read(file_path)

    # Extract scaled coordinates
    xs = laz.x
    ys = laz.y
    zs = laz.z

    min_x, max_x = xs.min(), xs.max()
    min_y, max_y = ys.min(), ys.max()

    # Compute scale factor
    scale_x = width / (max_x - min_x)
    scale_y = height / (max_y - min_y)
    scale_factor = min(scale_x, scale_y)

    # Transform and scale coordinates
    points = []
    for x, y, z in zip(xs, ys, zs):
        x_scaled = (x - min_x) * scale_factor
        y_scaled = (max_y - y) * scale_factor  # Pyqt Canvas has inverted Y axis
        points.append(QPoint3DF(x_scaled, y_scaled, z))
    
    return points