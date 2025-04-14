
module mount_pir() {
    board_depth = 14;
    board_width = 10;
    board_height = 8;
    board_thickness = 1.5;
    board_margin = 1.0;
    margin = 0.2;
    wall_thickness = 1.4;
    
    d1 = board_depth;
    w1 = board_width + 2*margin + 2*wall_thickness;
    h1 = board_height + 2*wall_thickness;
    
    d2 = d1 + 2;
    w2 = board_width + 2*margin;
    h2 = board_thickness + 2*margin;
    
    d3 = d1 + 2;
    w3 = w2 - 2*board_margin + 2*margin;
    h3 = h1 - 2*wall_thickness;
    
    difference() {
        // main box
        color("#77e")
        translate([-d1, -w1/2, 0])
        cube([d1, w1, h1]);
        
        // cut board
        color("#cce")
        translate([-d2+1, -w2/2, 5.5])
        cube([d2, w2, h2]);
        
        // cut board right side
        color("#cce")
        translate([-d2+1, -w2/2+board_margin, board_height-2*margin-0.3])
        cube([d2, w2-board_margin, h2-margin+0.4]);
        
        // cut front/back
        color("#cce")
        translate([-d3+1, -w3/2, wall_thickness])
        cube([d3, w3, h3]);
    }
}

mount_pir();