# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Overwatch Instant Ik",
    "author" : "Sxlar3d", 
    "description" : "Creates A Ik Rig For Overwatch Models",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
class SNA_PT_OW_IK__SXLAR3D_EC3B2(bpy.types.Panel):
    bl_label = 'Ow Ik - Sxlar3d'
    bl_idname = 'SNA_PT_OW_IK__SXLAR3D_EC3B2'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Ow Ik'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout.label(text='Overwatch Ik Rig', icon_value=241)
        op = layout.operator('sna.create_rig_505a9', text='Create Ik Rig', icon_value=0, emboss=True, depress=False)


class SNA_OT_Create_Rig_505A9(bpy.types.Operator):
    bl_idname = "sna.create_rig_505a9"
    bl_label = "Create Rig"
    bl_description = "Creates A Ik Rig For Overwatch Models"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os

        def append_object_from_addon_file(object_name):
            # Check if the object already exists in the scene
            if object_name in bpy.data.objects:
                return  # Return without doing anything if the object already exists
            # Get the filepath to the blend file in the models folder of the addon
            addon_folder = os.path.dirname(__file__)
            model_folder = os.path.join(addon_folder, "models")
            filepath = os.path.join(model_folder, "new rig bones.blend")
             # Append the object from the blend file
            with bpy.data.libraries.load(filepath) as (data_from, data_to):
                data_to.objects = [object_name]
            # Add the object to the scene
            bpy.context.view_layer.active_layer_collection.collection.objects.link(bpy.data.objects[object_name])
        # Example usage: append an object named "Cube" from the blend file in the models folder
        append_object_from_addon_file("RIG_Torso")
        append_object_from_addon_file("RIG_Tweak")
        append_object_from_addon_file("RIG_Toe")
        append_object_from_addon_file("RIG_Thumb")
        append_object_from_addon_file("RIG_Shoulder")
        append_object_from_addon_file("RIG_Root")
        append_object_from_addon_file("RIG_JawBone")
        append_object_from_addon_file("RIG_Index")
        append_object_from_addon_file("RIG_Hips")
        append_object_from_addon_file("RIG_Hand")
        append_object_from_addon_file("RIG_Forearm")
        append_object_from_addon_file("RIG_FootR")
        append_object_from_addon_file("RIG_FootL")
        append_object_from_addon_file("RIG_FingerRotR")
        append_object_from_addon_file("RIG_FaceBone")
        append_object_from_addon_file("RIG_EyeTrackMid")
        # Enter pose mode
        bpy.ops.object.mode_set(mode='POSE')
        # Get a reference to the active object and its pose bones
        obj = bpy.context.active_object
        pose_bones = obj.pose.bones
        bone_mapping = {
            "bone_001C": "hand_l",
            "bone_005A": "foot_l",
            "bone_0064": "foot_r",
            "bone_0063": "calf_r",
            "bone_0059": "calf_l",
            "bone_003A": "hand_r",
            "bone_0001": "root",
            "bone_0002": "pelvis",
            "bone_0003": "spine_01",
            "bone_0004": "spine_02",
            "bone_0005": "spine_03",
            "bone_0036": "upperarm_r",
            "bone_000D": "upperarm_l",
            "bone_0035": "clavicle_r",
            "bone_0050": "clavicle_l",
            "bone_0010": "neck_01",
            "bone_0011": "head",
            "bone_0037": "elbow_r",
            "bone_000E": "elbow_l",
            "bone_005B": "Toe_l",
            "bone_0065": "Toe_r",
        }
        # Iterate over the bone mapping
        for old_name, new_name in bone_mapping.items():
            # Select the bone
            bone = pose_bones[old_name]
            bone.bone.select = True
            # Rename the bone
            bone.name = new_name
        # Deselect all bones
        bpy.ops.pose.select_all(action='DESELECT')
        # Select the "hand_l" bone
        armature = bpy.context.active_object
        armature.data.bones['hand_l'].select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Get a reference to the active object and its edit bones
        obj = bpy.context.active_object
        edit_bones = obj.data.edit_bones
        # Deselect all bones
        for bone in edit_bones:
            bone.select = False
        # Select the bone named "hand_l"
        edit_bones["hand_l"].select = True
        # Duplicate the bone
        bpy.ops.armature.duplicate()
        # Rename the duplicated bone
        duplicated_bone = edit_bones[-1]
        duplicated_bone.name = "ik_hand_gun_l"
        # Set the parent of the duplicated bone to the "root" bone
        duplicated_bone.parent = edit_bones["root"]
        # Select the bone named "hand_l"
        edit_bones["ik_hand_gun_l"].select = True
        # Duplicate the bone
        bpy.ops.armature.duplicate()
        # Rename the duplicated bone
        duplicated_bone = edit_bones[-1]
        duplicated_bone.name = "ik_hand_l"
        # Set the parent of the duplicated bone to the "root" bone
        duplicated_bone.parent = edit_bones["ik_hand_gun_l"]
        # Get the armature object and its edit bones
        armature = bpy.context.active_object
        edit_bones = armature.data.edit_bones
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['elbow_l'].select_tail = True
        # Extrude Bone
        bpy.ops.armature.extrude_move(
            ARMATURE_OT_extrude={"forked":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                "orient_axis_ortho":'X',
                "orient_type":'GLOBAL',
                "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                "orient_matrix_type":'GLOBAL',
                "constraint_axis":(False, False, False),
                "mirror":False,
                "use_proportional_edit":False,
                "proportional_edit_falloff":'SMOOTH',
                "proportional_size":1,
                "use_proportional_connected":False,
                "use_proportional_projected":False,
                "snap":False,
                "snap_elements":{'INCREMENT'},
                "use_snap_project":False,
                "snap_target":'CLOSEST',
                "use_snap_self":True,
                "use_snap_edit":True,
                "use_snap_nonedit":True,
                "use_snap_selectable":False,
                "snap_point":(0, 0, 0),
                "snap_align":False,
                "snap_normal":(0, 0, 0),
                "gpencil_strokes":False,
                "cursor_transform":False,
                "texture_space":False,
                "remove_on_cancel":False,
                "view2d_edge_pan":False,
                "release_confirm":False,
                "use_accurate":False,
                "use_automerge_and_split":False
            }
        )
        #Move extruded bone
        bpy.ops.transform.translate(value=(0, 0.0981695, 0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "elbow_l.001"
        edit_bones["elbow_l.001"].select_head = True
        edit_bones["elbow_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(0, 0.881883, 0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_arm_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['calf_l'].select_tail = True
        #Extrude Calf_l
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Move extruded bone
        bpy.ops.transform.translate(value=(0, -0.141364, 0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_l.001"
        edit_bones["calf_l.001"].select_head = True
        edit_bones["calf_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Move the calf_l.001
        bpy.ops.transform.translate(value=(-0, -0.965847, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_leg_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Get a reference to the active object and its edit bones
        obj = bpy.context.active_object
        edit_bones = obj.data.edit_bones
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.ops.object.posemode_toggle()
        # Get a reference to the active object and its pose bones
        obj = bpy.context.active_object
        pose_bones = obj.pose.bones
        armature = bpy.context.active_object
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Select the "foot_l" bone
        pose_bones['foot_l'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(
            ARMATURE_OT_duplicate={"do_flip_names":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                "orient_axis_ortho":'X',
                "orient_type":'GLOBAL',
                "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                "orient_matrix_type":'GLOBAL',
                "constraint_axis":(False, False, False),
                "mirror":False,
                "use_proportional_edit":False,
                "proportional_edit_falloff":'SMOOTH',
                "proportional_size":1,
                "use_proportional_connected":False,
                "use_proportional_projected":False,
                "snap":False,
                "snap_elements":{'INCREMENT'},
                "use_snap_project":False,
                "snap_target":'CLOSEST',
                "use_snap_self":True,
                "use_snap_edit":True,
                "use_snap_nonedit":True,
                "use_snap_selectable":False,
                "snap_point":(0, 0, 0),
                "snap_align":False,
                "snap_normal":(0, 0, 0),
                "gpencil_strokes":False,
                "cursor_transform":False,
                "texture_space":False,
                "remove_on_cancel":False,
                "view2d_edge_pan":False,
                "release_confirm":False,
                "use_accurate":False,
                "use_automerge_and_split":False
            }
        )
        # Get the armature object and its edit bones
        edit_bones = armature.data.edit_bones
        # Select the newly duplicated bone
        edit_bones[-1].select = True
        # Rename the newly duplicated bone
        edit_bones[-1].name = "ik_foot_l"
        # Set the parent of the newly duplicated bone to the "root" bone
        edit_bones["ik_foot_l"].parent = edit_bones["root"]
        # Get a reference to the active object and its edit bones
        obj = bpy.context.active_object
        edit_bones = obj.data.edit_bones
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.ops.object.posemode_toggle()
        # Get a reference to the active object and its pose bones
        obj = bpy.context.active_object
        pose_bones = obj.pose.bones
        armature = bpy.context.active_object
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Select the "hand_r" bone
        pose_bones['hand_r'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(
            ARMATURE_OT_duplicate={"do_flip_names":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                "orient_axis_ortho":'X',
                "orient_type":'GLOBAL',
                "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                "orient_matrix_type":'GLOBAL',
                "constraint_axis":(False, False, False),
                "mirror":False,
                "use_proportional_edit":False,
                "proportional_edit_falloff":'SMOOTH',
                "proportional_size":1,
                "use_proportional_connected":False,
                "use_proportional_projected":False,
                "snap":False,
                "snap_elements":{'INCREMENT'},
                "use_snap_project":False,
                "snap_target":'CLOSEST',
                "use_snap_self":True,
                "use_snap_edit":True,
                "use_snap_nonedit":True,
                "use_snap_selectable":False,
                "snap_point":(0, 0, 0),
                "snap_align":False,
                "snap_normal":(0, 0, 0),
                "gpencil_strokes":False,
                "cursor_transform":False,
                "texture_space":False,
                "remove_on_cancel":False,
                "view2d_edge_pan":False,
                "release_confirm":False,
                "use_accurate":False,
                "use_automerge_and_split":False
            }
        )
        # Get the armature object and its edit bones
        edit_bones = armature.data.edit_bones
        # Select the newly duplicated bone
        edit_bones[-1].select = True
        # Rename the newly duplicated bone
        edit_bones[-1].name = "ik_hand_gun_r"
        # Set the parent of the newly duplicated bone to the "root" bone
        edit_bones["ik_hand_gun_r"].parent = edit_bones["root"]
        # Select the bone named "hand_l"
        edit_bones["ik_hand_gun_r"].select = True
        # Duplicate the bone
        bpy.ops.armature.duplicate()
        # Rename the duplicated bone
        duplicated_bone = edit_bones[-1]
        duplicated_bone.name = "ik_hand_r"
        # Set the parent of the duplicated bone to the "ik_hand_gun_r" bone
        duplicated_bone.parent = edit_bones["ik_hand_gun_r"]
        # Get the armature object and its edit bones
        armature = bpy.context.active_object
        edit_bones = armature.data.edit_bones
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['elbow_r'].select_tail = True
        # Extrude the bone
        bpy.ops.armature.extrude_move(
            ARMATURE_OT_extrude={"forked":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                "orient_axis_ortho":'X',
                "orient_type":'GLOBAL',
                "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                "orient_matrix_type":'GLOBAL',
                "constraint_axis":(False, False, False),
                "mirror":False,
                "use_proportional_edit":False,
                "proportional_edit_falloff":'SMOOTH',
                "proportional_size":1,
                "use_proportional_connected":False,
                "use_proportional_projected":False,
                "snap":False,
                "snap_elements":{'INCREMENT'},
                "use_snap_project":False,
                "snap_target":'CLOSEST',
                "use_snap_self":True,
                "use_snap_edit":True,
                "use_snap_nonedit":True,
                "use_snap_selectable":False,
                "snap_point":(0, 0, 0),
                "snap_align":False,
                "snap_normal":(0, 0, 0),
                "gpencil_strokes":False,
                "cursor_transform":False,
                "texture_space":False,
                "remove_on_cancel":False,
                "view2d_edge_pan":False,
                "release_confirm":False,
                "use_accurate":False,
                "use_automerge_and_split":False
            }
        )
        # Translate the object along the Y axis
        bpy.ops.transform.translate(
            value=(0, 0.0834512, 0),
            orient_axis_ortho='X',
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, True, False),
            mirror=False,
            snap=False,
            snap_elements={'INCREMENT'},
            use_snap_project=False,
            snap_target='CLOSEST',
            use_snap_self=True,
            use_snap_edit=True,
            use_snap_nonedit=True,
            use_snap_selectable=False,
            release_confirm=True
        )
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "elbow_r.001"
        edit_bones["elbow_r.001"].select_head = True
        edit_bones["elbow_r.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the object
        bpy.ops.transform.translate(
            value=(0, 0.894303, 0),
            orient_axis_ortho='X',
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, True, False),
            mirror=False,
            snap=False,
            snap_elements={'INCREMENT'},
            use_snap_project=False,
            snap_target='CLOSEST',
            use_snap_self=True,
            use_snap_edit=True,
            use_snap_nonedit=True,
            use_snap_selectable=False,
            release_confirm=True
        )
        bpy.context.active_bone.name = "pole_arm_r"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['calf_r'].select_tail = True
        # Extrude and move the selected bone
        bpy.ops.armature.extrude_move(
            ARMATURE_OT_extrude={"forked":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                "orient_axis_ortho":'X',
                "orient_type":'GLOBAL',
                "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                "orient_matrix_type":'GLOBAL',
                "constraint_axis":(False, False, False),
                "mirror":False,
                "use_proportional_edit":False,
                "proportional_edit_falloff":'SMOOTH',
                "proportional_size":1,
                "use_proportional_connected":False,
                "use_proportional_projected":False,
                "snap":False,
                "snap_elements":{'INCREMENT'},
                "use_snap_project":False,
                "snap_target":'CLOSEST',
                "use_snap_self":True,
                "use_snap_edit":True,
                "use_snap_nonedit":True,
                "use_snap_selectable":False,
                "snap_point":(0, 0, 0),
                "snap_align":False,
                "snap_normal":(0, 0, 0),
                "gpencil_strokes":False,
                "cursor_transform":False,
                "texture_space":False,
                "remove_on_cancel":False,
                "view2d_edge_pan":False,
                "release_confirm":False,
                "use_accurate":False,
                "use_automerge_and_split":False
            }
        )
        # Perform the translate operation
        bpy.ops.transform.translate(value=(-0, -0.14376, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_r.001"
        edit_bones["calf_r.001"].select_head = True
        edit_bones["calf_r.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(-0, -0.972968, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_leg_r"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Get a reference to the active object and its edit bones
        obj = bpy.context.active_object
        edit_bones = obj.data.edit_bones
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.ops.object.posemode_toggle()
        # Get a reference to the active object and its pose bones
        obj = bpy.context.active_object
        pose_bones = obj.pose.bones
        armature = bpy.context.active_object
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Select the "foot_r" bone
        pose_bones['foot_r'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(
            ARMATURE_OT_duplicate={"do_flip_names":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                "orient_axis_ortho":'X',
                "orient_type":'GLOBAL',
                "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                "orient_matrix_type":'GLOBAL',
                "constraint_axis":(False, False, False),
                "mirror":False,
                "use_proportional_edit":False,
                "proportional_edit_falloff":'SMOOTH',
                "proportional_size":1,
                "use_proportional_connected":False,
                "use_proportional_projected":False,
                "snap":False,
                "snap_elements":{'INCREMENT'},
                "use_snap_project":False,
                "snap_target":'CLOSEST',
                "use_snap_self":True,
                "use_snap_edit":True,
                "use_snap_nonedit":True,
                "use_snap_selectable":False,
                "snap_point":(0, 0, 0),
                "snap_align":False,
                "snap_normal":(0, 0, 0),
                "gpencil_strokes":False,
                "cursor_transform":False,
                "texture_space":False,
                "remove_on_cancel":False,
                "view2d_edge_pan":False,
                "release_confirm":False,
                "use_accurate":False,
                "use_automerge_and_split":False
            }
        )
        # Get the armature object and its edit bones
        edit_bones = armature.data.edit_bones
        # Select the newly duplicated bone
        edit_bones[-1].select = True
        # Rename the newly duplicated bone
        edit_bones[-1].name = "ik_foot_r"
        # Set the parent of the newly duplicated bone to the "root" bone
        edit_bones["ik_foot_r"].parent = edit_bones["root"]
        # Get a reference to the active object and its edit bones
        obj = bpy.context.active_object
        edit_bones = obj.data.edit_bones
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.ops.object.posemode_toggle()
        # Get a reference to the active object and its pose bones
        obj = bpy.context.active_object
        pose_bones = obj.pose.bones
        armature = bpy.context.active_object
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "ik_hand_l"
        armature.data.bones.active = armature.data.bones["ik_hand_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Shift-click the "hand_l" bone
        armature.data.bones.active = armature.data.bones["hand_l"]
        bpy.ops.pose.select_all(action='INVERT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.ik_add(with_targets=True)
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "hand_l" bone to the active armature
        ik_constraint = armature.pose.bones["hand_l"].constraints["IK"]
        ik_constraint.target = armature
        ik_constraint.pole_target = armature
        # Set the target bone and pole target bone of the IK constraint to "ik_hand_l" and "pole_arm_l", respectively
        ik_constraint.subtarget = "ik_hand_l"
        ik_constraint.pole_subtarget = "pole_arm_l"
        # Set the chain length of the IK constraint to 3
        ik_constraint.chain_count = 3
        # Enable rotation in the IK constraint
        ik_constraint.use_rotation = True
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "ik_hand_r"
        armature.data.bones.active = armature.data.bones["ik_hand_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Shift-click the "hand_r" bone
        armature.data.bones.active = armature.data.bones["hand_r"]
        bpy.ops.pose.select_all(action='INVERT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.ik_add(with_targets=True)
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "hand_r" bone to the active armature
        ik_constraint = armature.pose.bones["hand_r"].constraints["IK"]
        ik_constraint.target = armature
        ik_constraint.pole_target = armature
        # Set the target bone and pole target bone of the IK constraint to "ik_hand_r" and "pole_arm_r", respectively
        ik_constraint.subtarget = "ik_hand_r"
        ik_constraint.pole_subtarget = "pole_arm_r"
        # Set the chain length of the IK constraint to 3
        ik_constraint.chain_count = 3
        # Enable rotation in the IK constraint
        ik_constraint.use_rotation = True
        # Set the pole angle of the IK constraint to 180
        ik_constraint.pole_angle = 180
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "ik_foot_l"
        armature.data.bones.active = armature.data.bones["ik_foot_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Shift-click the "foot_l" bone
        armature.data.bones.active = armature.data.bones["foot_l"]
        bpy.ops.pose.select_all(action='INVERT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.ik_add(with_targets=True)
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_l" bone to the active armature
        ik_constraint = armature.pose.bones["foot_l"].constraints["IK"]
        ik_constraint.target = armature
        ik_constraint.pole_target = armature
        # Set the target bone and pole target bone of the IK constraint to "ik_foot_l" and "pole_leg_l", respectively
        ik_constraint.subtarget = "ik_foot_l"
        ik_constraint.pole_subtarget = "pole_leg_l"
        # Set the chain length of the IK constraint to 3
        ik_constraint.chain_count = 3
        # Enable rotation in the IK constraint
        ik_constraint.use_rotation = True
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "ik_foot_r"
        armature.data.bones.active = armature.data.bones["ik_foot_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Shift-click the "foot_r" bone
        armature.data.bones.active = armature.data.bones["foot_r"]
        bpy.ops.pose.select_all(action='INVERT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.ik_add(with_targets=True)
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        ik_constraint = armature.pose.bones["foot_r"].constraints["IK"]
        ik_constraint.target = armature
        ik_constraint.pole_target = armature
        # Set the target bone and pole target bone of the IK constraint to "ik_foot_r" and "pole_leg_r", respectively
        ik_constraint.subtarget = "ik_foot_r"
        ik_constraint.pole_subtarget = "pole_leg_r"
        # Set the chain length of the IK constraint to 3
        ik_constraint.chain_count = 3
        # Enable rotation in the IK constraint
        ik_constraint.use_rotation = True
        # Set the pole angle of the IK constraint to 180
        ik_constraint.pole_angle = 180
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Get all objects in the scene
        objects = bpy.data.objects
        # Iterate over all objects
        for obj in objects:
            # Check if the object is an empty
            if obj.type == 'EMPTY':
                # Delete the empty object
                bpy.data.objects.remove(obj, do_unlink=True)
        # Set the active bone to "pole_leg_l"
        armature.data.bones.active = armature.data.bones["pole_leg_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Tweak"]
        # Set the active bone to "pole_leg_r"
        armature.data.bones.active = armature.data.bones["pole_leg_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Tweak"]
        # Set the active bone to "pole_arm_l"
        armature.data.bones.active = armature.data.bones["pole_arm_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Tweak"]
        # Set the active bone to "pole_arm_r"
        armature.data.bones.active = armature.data.bones["pole_arm_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Tweak"]
        # Set the active bone to "clavicle_l"
        armature.data.bones.active = armature.data.bones["clavicle_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Shoulder"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = -1.5708
        # Set the active bone to "clavicle_r"
        armature.data.bones.active = armature.data.bones["clavicle_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Shoulder"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = 1.5708
        # Set the active bone to "ik_hand_l"
        armature.data.bones.active = armature.data.bones["ik_hand_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hand"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = -1.5708
        # Set the active bone to "ik_hand_r"
        armature.data.bones.active = armature.data.bones["ik_hand_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hand"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = 1.5708
        # Set the active bone to "root"
        armature.data.bones.active = armature.data.bones["root"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Root"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 20
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 20
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 20
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = 1.5708
        # Set the active bone to "ik_foot_l"
        armature.data.bones.active = armature.data.bones["ik_foot_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_FootL"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = 1.5708
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = -3.14159
        # Set the active bone to "ik_foot_r"
        armature.data.bones.active = armature.data.bones["ik_foot_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_FootR"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = -1.5708
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = -3.14159
        # Set the active bone to "pelvis"
        armature.data.bones.active = armature.data.bones["pelvis"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Torso"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 200
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 200
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 200
        # Set the active bone to "spine_01"
        armature.data.bones.active = armature.data.bones["spine_01"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        # Set the active bone to "spine_02"
        armature.data.bones.active = armature.data.bones["spine_02"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 100
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 100
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 100
        # Set the active bone to "spine_03"
        armature.data.bones.active = armature.data.bones["spine_03"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 85
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 85
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 85
        # Set the active bone to "Toe_l"
        armature.data.bones.active = armature.data.bones["Toe_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Toe"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = -1.5708
        # Set the active bone to "Toe_r"
        armature.data.bones.active = armature.data.bones["Toe_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Toe"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = 1.5708
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = 3.14159
        # Set the active bone to "neck_01"
        armature.data.bones.active = armature.data.bones["neck_01"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 100
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 100
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 100
        # Set the active bone to "head"
        armature.data.bones.active = armature.data.bones["head"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 50
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 50
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 50
        # Deselect all bones in pose mode
        bpy.ops.pose.select_all(action='DESELECT')
        # Switch to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
        # Deselect everything in object mode
        bpy.ops.object.select_all(action='DESELECT')
        # Select all objects that have the word "RIG" in their name
        for obj in bpy.data.objects:
            if "hardpoint" in obj.name:
                obj.select_set(True)
        # Use the "H" shortcut to hide the selected objects
        bpy.ops.object.hide_view_set(unselected=False)
        # Deselect everything in object mode
        bpy.ops.object.select_all(action='DESELECT')
        # Select all objects that have the word "RIG" in their name
        for obj in bpy.data.objects:
            if "RIG" in obj.name:
                obj.select_set(True)
        # Use the "H" shortcut to hide the selected objects
        bpy.ops.object.hide_view_set(unselected=False)
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_PT_OW_IK__SXLAR3D_EC3B2)
    bpy.utils.register_class(SNA_OT_Create_Rig_505A9)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_PT_OW_IK__SXLAR3D_EC3B2)
    bpy.utils.unregister_class(SNA_OT_Create_Rig_505A9)
