
module mount_heat_camera_support(size, thickness) {
    color("#44e")
    rotate(90, [1, 0, 0])
    linear_extrude(thickness)
    polygon([
        [0, 0],
        [0, size],
        [-size*0.49, 0],
    ]);
}

module mount_heat_camera() {
    board_width = 18.2;
    board_height = 17.3;
    board_thickness = 1.5;
    board_margin = 1.4;
    margin = 0.2;
    wall_thickness = 1.4;
    
    d1 = board_thickness + 2*margin + 2*wall_thickness;
    w1 = board_width + 2*margin + 2*wall_thickness;
    h1 = board_height + margin + wall_thickness;
    
    d2 = board_thickness + 2*margin;
    w2 = board_width + 2*margin;
    h2 = board_height + margin + 0.001;
    
    d3 = d1 + 1;
    w3 = board_width - 2*board_margin + 2*margin;
    h3 = h2;
    
    difference() {
        // main box
        color("#77e")
        translate([0, -w1/2, 0])
        cube([d1, w1, h1]);
        
        // cut board
        color("#cce")
        translate([-d2/2+d1/2, -w2/2, wall_thickness])
        cube([d2, w2, h2]);
        
        // cut front/back
        color("#cce")
        translate([-d3/2+d1/2, -w3/2, wall_thickness])
        cube([d3, w3, h3]);
    }
    
    translate([0, w1/2, 0])
    mount_heat_camera_support(h1, wall_thickness);
    translate([0, -w1/2+wall_thickness, 0])
    mount_heat_camera_support(h1, wall_thickness);
}

mount_heat_camera();