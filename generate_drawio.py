import os
import uuid

def generate_drawio_xml(name, user_steps, system_steps):
    # Template header
    xml = f"""<mxfile host="65bd71144e">
    <diagram id="{uuid.uuid4()}" name="{name}">
        <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="parent_swimlane" value="{name}" style="swimlane;html=1;childLayout=stackLayout;horizontal=1;startSize=20;horizontalStack=1;resizeParent=1;resizeParentMax=0;resizeLast=1;collapsible=1;marginBottom=0;" vertex="1" parent="1">
                    <mxGeometry x="40" y="40" width="800" height="{(len(user_steps) + len(system_steps)) * 130 + 200}" as="geometry"/>
                </mxCell>
                <mxCell id="lane_pengguna" value="Pengguna" style="swimlane;html=1;startSize=20;" vertex="1" parent="parent_swimlane">
                    <mxGeometry x="0" y="20" width="400" height="{(len(user_steps) + len(system_steps)) * 130 + 180}" as="geometry"/>
                </mxCell>
                <mxCell id="lane_sistem" value="Sistem" style="swimlane;html=1;startSize=20;" vertex="1" parent="parent_swimlane">
                    <mxGeometry x="400" y="20" width="400" height="{(len(user_steps) + len(system_steps)) * 130 + 180}" as="geometry"/>
                </mxCell>
    """

    y_pos = 50
    current_id = 10

    # Start node (Pengguna)
    start_id = current_id
    xml += f"""            <mxCell id="{start_id}" value="" style="ellipse;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane_pengguna">
                    <mxGeometry x="185" y="{y_pos}" width="30" height="30" as="geometry"/>
                </mxCell>
    """
    y_pos += 80
    current_id += 1

    last_node_id = start_id
    last_lane = "lane_pengguna"

    # Alternate steps for simplicity in this generator, or just do all user then all system
    # Let's try to weave them if they are roughly the same length

    all_steps = []
    # Mix them: first user, then first system, etc.
    max_len = max(len(user_steps), len(system_steps))
    for i in range(max_len):
        if i < len(user_steps):
            all_steps.append(("Pengguna", user_steps[i].strip()))
        if i < len(system_steps):
            all_steps.append(("Sistem", system_steps[i].strip()))

    for lane_name, step_text in all_steps:
        lane_id = "lane_pengguna" if lane_name == "Pengguna" else "lane_sistem"
        node_id = current_id
        xml += f"""            <mxCell id="{node_id}" value="{step_text}" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="{lane_id}">
                    <mxGeometry x="100" y="{y_pos}" width="200" height="60" as="geometry"/>
                </mxCell>
        """

        # Add edge from last node
        edge_id = current_id + 1000
        # If jumping lanes, the source and target parents are different, need to handle relative coords?
        # Drawio usually handles this if parent is the lane.
        # But for edges between lanes, sometimes it's better to have them under parent_swimlane or root 1.
        # Let's put edges under root 1 for simplicity of coordinate management.

        xml += f"""            <mxCell id="{edge_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="{last_node_id}" target="{node_id}">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
        """

        last_node_id = node_id
        current_id += 1
        y_pos += 120

    # End node (Pengguna)
    end_id = current_id
    xml += f"""            <mxCell id="{end_id}" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane_pengguna">
                    <mxGeometry x="185" y="{y_pos}" width="30" height="30" as="geometry"/>
                </mxCell>
                <mxCell id="{current_id + 2000}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="{last_node_id}" target="{end_id}">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
    """

    # Closing tags
    xml += """            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
"""
    return xml

def main():
    with open('activity_spec.txt', 'r') as f:
        content = f.read()

    activities = content.split('Activity: ')
    for act in activities:
        if not act.strip():
            continue

        lines = act.strip().split('\n')
        name = lines[0].strip()
        user_steps = []
        system_steps = []

        for line in lines[1:]:
            if line.startswith('Pengguna: '):
                user_steps = line.replace('Pengguna: ', '').split(',')
            elif line.startswith('Sistem: '):
                system_steps = line.replace('Sistem: ', '').split(',')

        filename = f"activity_{name.lower().replace(' ', '_')}.drawio"
        filepath = os.path.join('diagram/activity', filename)

        xml_content = generate_drawio_xml(name, user_steps, system_steps)

        with open(filepath, 'w') as f_out:
            f_out.write(xml_content)
        print(f"Generated {filepath}")

if __name__ == "__main__":
    main()
