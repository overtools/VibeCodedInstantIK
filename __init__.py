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
    "name" : "Overwatch Instant Ik Fix made by Tevtongermany for blender 4.0",
    "author" : "Sxlar3d, Tevtongermany", 
    "description" : "Creates A Ik Rig For Overwatch Models, quick note IK and FK switch might not work but if they do ig its good",
    "blender" : (4, 0, 0),
    "version" : (1, 3, 0),
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
class SNA_OT_Create_Orisa_Rig_6B0F4(bpy.types.Operator):
    bl_idname = "sna.create_orisa_rig_6b0f4"
    bl_label = "Create Orisa Rig"
    bl_description = "Creates a Unique Rig For Orisa"
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
            "bone_0194": "back_foot_l",
            "bone_0195": "back_foot_r",
            "bone_018D": "back_calf_r",
            "bone_018C": "back_calf_l",
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
        bpy.ops.transform.translate(value=(0, 0.0981695, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "elbow_l.001"
        edit_bones["elbow_l.001"].select_head = True
        edit_bones["elbow_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(0, 0.881883, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_arm_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['calf_l'].select_tail = True
        #Extrude Calf_l
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),   "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Move extruded bone
        bpy.ops.transform.translate(value=(0, -0.141364, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_l.001"
        edit_bones["calf_l.001"].select_head = True
        edit_bones["calf_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Move the calf_l.001
        bpy.ops.transform.translate(value=(0, 1.85873, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_leg_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['back_calf_r'].select_tail = True
        #Extrude back_calf_r
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),   "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Move extruded bone
        bpy.ops.transform.translate(value=(0, 0.147272, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "back_calf_r.001"
        edit_bones["back_calf_r.001"].select_head = True
        edit_bones["back_calf_r.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Move the back_calf_r.001
        bpy.ops.transform.translate(value=(0, 1.3125, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_back_leg_r"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['back_calf_l'].select_tail = True
        #Extrude back_calf_l
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),   "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Move extruded bone
        bpy.ops.transform.translate(value=(0, 0.189511, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "back_calf_l.001"
        edit_bones["back_calf_l.001"].select_head = True
        edit_bones["back_calf_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Move the back_calf_l.001
        bpy.ops.transform.translate(value=(0, 1.29409, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_back_leg_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
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
        bpy.ops.transform.translate(value=(-0, -0.14376, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_r.001"
        edit_bones["calf_r.001"].select_head = True
        edit_bones["calf_r.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(0, 1.86382, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
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
        # Select the "back_foot_l" bone
        pose_bones['back_foot_l'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(
            ARMATURE_OT_duplicate={"do_flip_names":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                 
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
        edit_bones[-1].name = "ik_back_foot_l"
        # Set the parent of the newly duplicated bone to the "root" bone
        edit_bones["ik_back_foot_l"].parent = edit_bones["root"]
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
        # Select the "back_foot_r" bone
        pose_bones['back_foot_r'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(
            ARMATURE_OT_duplicate={"do_flip_names":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                 
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
        edit_bones[-1].name = "ik_back_foot_r"
        # Set the parent of the newly duplicated bone to the "root" bone
        edit_bones["ik_back_foot_r"].parent = edit_bones["root"]
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
        # Set the active bone to "ik_back_foot_l"
        armature.data.bones.active = armature.data.bones["ik_back_foot_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Shift-click the "back_foot_l" bone
        armature.data.bones.active = armature.data.bones["back_foot_l"]
        bpy.ops.pose.select_all(action='INVERT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.ik_add(with_targets=True)
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "back_foot_l" bone to the active armature
        ik_constraint = armature.pose.bones["back_foot_l"].constraints["IK"]
        ik_constraint.target = armature
        ik_constraint.pole_target = armature
        # Set the target bone and pole target bone of the IK constraint to "ik_back_foot_l" and "pole_back_leg_l", respectively
        ik_constraint.subtarget = "ik_back_foot_l"
        ik_constraint.pole_subtarget = "pole_back_leg_l"
        # Set the chain length of the IK constraint to 3
        ik_constraint.chain_count = 3
        # Enable rotation in the IK constraint
        ik_constraint.use_rotation = True
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "ik_back_foot_r"
        armature.data.bones.active = armature.data.bones["ik_back_foot_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Shift-click the "back_foot_r" bone
        armature.data.bones.active = armature.data.bones["back_foot_r"]
        bpy.ops.pose.select_all(action='INVERT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.ik_add(with_targets=True)
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "back_foot_r" bone to the active armature
        ik_constraint = armature.pose.bones["back_foot_r"].constraints["IK"]
        ik_constraint.target = armature
        ik_constraint.pole_target = armature
        # Set the target bone and pole target bone of the IK constraint to "ik_back_foot_r" and "pole_back_leg_r", respectively
        ik_constraint.subtarget = "ik_back_foot_r"
        ik_constraint.pole_subtarget = "pole_back_leg_r"
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
        # Set the active bone to "pole_back_leg_l"
        armature.data.bones.active = armature.data.bones["pole_back_leg_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Tweak"]
        # Set the active bone to "pole_back_leg_r"
        armature.data.bones.active = armature.data.bones["pole_back_leg_r"]
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
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 200
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 200
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 200
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = -1.5708
        # Set the active bone to "clavicle_r"
        armature.data.bones.active = armature.data.bones["clavicle_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Shoulder"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 200
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 200
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 200
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
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 1000
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 1000
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 1000
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
        # Set the active bone to "ik_back_foot_l"
        armature.data.bones.active = armature.data.bones["ik_back_foot_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_FootL"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 150
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 150
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 150
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = 4.71239
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = -3.14159
        # Set the active bone to "ik_back_foot_r"
        armature.data.bones.active = armature.data.bones["ik_back_foot_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_FootR"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 150
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 150
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 150
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = 1.5708
        bpy.context.active_pose_bone.custom_shape_rotation_euler[2] = -3.14159
        # Set the active bone to "pelvis"
        armature.data.bones.active = armature.data.bones["pelvis"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Torso"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 300
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 300
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 300
        # Set the active bone to "spine_01"
        armature.data.bones.active = armature.data.bones["spine_01"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 180
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 180
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 180
        # Set the active bone to "spine_02"
        armature.data.bones.active = armature.data.bones["spine_02"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 180
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 180
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 180
        # Set the active bone to "spine_03"
        armature.data.bones.active = armature.data.bones["spine_03"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Hips"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 120
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 120
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


class SNA_OT_Create_Junkrat_Rig_Af672(bpy.types.Operator):
    bl_idname = "sna.create_junkrat_rig_af672"
    bl_label = "Create Junkrat Rig"
    bl_description = "Creates a Ik Rig For Junkrat"
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
            "bone_0398": "eyebrow_r_down",
            "bone_039B": "eye_r",
            "bone_0399": "eyebrow_r_up",
            "bone_0397": "eyebrow_l_up",
            "bone_039A": "eye_l",
            "bone_0396": "eyebrow_l_down",
            "bone_03BC": "Jaw",
            "bone_0055": "leg_l",
            "bone_005F": "leg_r",
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
        bpy.ops.transform.translate(value=(0, 0.0981695, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "elbow_l.001"
        edit_bones["elbow_l.001"].select_head = True
        edit_bones["elbow_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(0, 0.881883, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_arm_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['bone_0016'].select_tail = True
        # Extrude Bone
        bpy.ops.armature.extrude_move(
            ARMATURE_OT_extrude={"forked":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
                 
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
        bpy.ops.transform.translate(value=(-0, -0.0350553, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "bone_0016.001"
        edit_bones["bone_0016.001"].select_head = True
        edit_bones["bone_0016.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(-0, -0.344345, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.ops.transform.translate(value=(-0, -0, -0.0132145),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "eye_follow"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
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
        pose_bones['eye_follow'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(ARMATURE_OT_duplicate={"do_flip_names":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),   "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Translate the selected bone
        bpy.ops.transform.translate(value=(-0.0316693, -0, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "eye_follow_r"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["eye_follow"]
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
        # Select the "eye_follow_r" bone
        pose_bones['eye_follow_r'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(ARMATURE_OT_duplicate={"do_flip_names":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),   "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Translate the selected bone
        bpy.ops.transform.translate(value=(0.0631107, 0, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "eye_follow_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["eye_follow"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['calf_l'].select_tail = True
        #Extrude Calf_l
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),   "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Move extruded bone
        bpy.ops.transform.translate(value=(0, -0.141364, 0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_l.001"
        edit_bones["calf_l.001"].select_head = True
        edit_bones["calf_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Move the calf_l.001
        bpy.ops.transform.translate(value=(-0, -0.965847, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
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
        bpy.ops.transform.translate(value=(-0, -0.14376, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_r.001"
        edit_bones["calf_r.001"].select_head = True
        edit_bones["calf_r.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(-0, -0.972968, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
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
        # Set the active bone to "eye_r"
        armature.data.bones.active = armature.data.bones["eye_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='TRACK_TO')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].target = armature
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].subtarget = "eye_follow_r"
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].use_target_z = True
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].target_space = 'POSE'
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].owner_space = 'POSE'
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eye_l"
        armature.data.bones.active = armature.data.bones["eye_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='TRACK_TO')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].target = armature
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].subtarget = "eye_follow_l"
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].target_space = 'POSE'
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].owner_space = 'POSE'
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].track_axis = 'TRACK_Z'
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_r_up"
        armature.data.bones.active = armature.data.bones["eyebrow_r_up"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].influence = 0.8
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].influence = 0.5
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_l_up"
        armature.data.bones.active = armature.data.bones["eyebrow_l_up"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].influence = 0.8
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].influence = 0.5
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_r_down"
        armature.data.bones.active = armature.data.bones["eyebrow_r_down"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].influence = 0.3
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].influence = 0.15
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_l_down"
        armature.data.bones.active = armature.data.bones["eyebrow_l_down"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].influence = 0.3
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].influence = 0.15
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
        # Set the active bone to "eye_follow_r"
        armature.data.bones.active = armature.data.bones["eye_follow_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Index"]
        # Set the active bone to "eye_follow_l"
        armature.data.bones.active = armature.data.bones["eye_follow_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Index"]
        # Set the active bone to "eye_follow"
        armature.data.bones.active = armature.data.bones["eye_follow"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_EyeTrackMid"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 20
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 20
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 20
        # Set the active bone to "Jaw"
        armature.data.bones.active = armature.data.bones["Jaw"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_JawBone"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 80
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 80
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 80
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = 2.0944
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
            "bone_0398": "eyebrow_r_down",
            "bone_039B": "eye_r",
            "bone_0399": "eyebrow_r_up",
            "bone_0397": "eyebrow_l_up",
            "bone_039A": "eye_l",
            "bone_0396": "eyebrow_l_down",
            "bone_03BC": "Jaw",
            "bone_0055": "leg_l",
            "bone_005F": "leg_r",
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
        bpy.ops.transform.translate(value=(0, 0.0981695, 0),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "elbow_l.001"
        edit_bones["elbow_l.001"].select_head = True
        edit_bones["elbow_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(0, 0.881883, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "pole_arm_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['bone_0016'].select_tail = True
        # Extrude Bone
        bpy.ops.armature.extrude_move(
            ARMATURE_OT_extrude={"forked":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, 0),
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
        bpy.ops.transform.translate(value=(-0, -0.0350553, -0),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "bone_0016.001"
        edit_bones["bone_0016.001"].select_head = True
        edit_bones["bone_0016.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(-0, -0.344345, -0),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.ops.transform.translate(value=(-0, -0, -0.0132145),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "eye_follow"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["root"]
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
        pose_bones['eye_follow'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(ARMATURE_OT_duplicate={"do_flip_names":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),  "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Translate the selected bone
        bpy.ops.transform.translate(value=(-0.0316693, -0, -0),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "eye_follow_r"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["eye_follow"]
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
        # Select the "eye_follow_r" bone
        pose_bones['eye_follow_r'].bone.select = True
        # Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Duplicate the bone
        bpy.ops.armature.duplicate_move(ARMATURE_OT_duplicate={"do_flip_names":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),   "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Translate the selected bone
        bpy.ops.transform.translate(value=(0.0631107, 0, 0),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        bpy.context.active_bone.name = "eye_follow_l"
        active_bone = bpy.context.active_bone
        active_bone.parent = edit_bones["eye_follow"]
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the end point of the bone
        edit_bones['calf_l'].select_tail = True
        #Extrude Calf_l
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0),  "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        # Move extruded bone
        bpy.ops.transform.translate(value=(0, -0.141364, 0),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_l.001"
        edit_bones["calf_l.001"].select_head = True
        edit_bones["calf_l.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Move the calf_l.001
        bpy.ops.transform.translate(value=(-0, -0.965847, -0),  orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
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
        bpy.ops.transform.translate(value=(-0, -0.14376, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        bpy.ops.armature.select_all(action='DESELECT')
        # Select the bone named "calf_r.001"
        edit_bones["calf_r.001"].select_head = True
        edit_bones["calf_r.001"].select_tail = True
        bpy.context.active_bone.use_connect = False
        # Translate the selected bone
        bpy.ops.transform.translate(value=(-0, -0.972968, -0),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
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
        # Set the active bone to "eye_r"
        armature.data.bones.active = armature.data.bones["eye_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='TRACK_TO')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].target = armature
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].subtarget = "eye_follow_r"
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].use_target_z = True
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].target_space = 'POSE'
        bpy.context.object.pose.bones["eye_r"].constraints["Track To"].owner_space = 'POSE'
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eye_l"
        armature.data.bones.active = armature.data.bones["eye_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='TRACK_TO')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].target = armature
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].subtarget = "eye_follow_l"
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].target_space = 'POSE'
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].owner_space = 'POSE'
        bpy.context.object.pose.bones["eye_l"].constraints["Track To"].track_axis = 'TRACK_Z'
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_r_up"
        armature.data.bones.active = armature.data.bones["eyebrow_r_up"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation"].influence = 0.8
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_up"].constraints["Copy Rotation.001"].influence = 0.5
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_l_up"
        armature.data.bones.active = armature.data.bones["eyebrow_l_up"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation"].influence = 0.8
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_up"].constraints["Copy Rotation.001"].influence = 0.5
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_r_down"
        armature.data.bones.active = armature.data.bones["eyebrow_r_down"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation"].influence = 0.3
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].subtarget = "eye_r"
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_r_down"].constraints["Copy Rotation.001"].influence = 0.15
        # Deselect all bones
        for bone in pose_bones:
            bone.bone.select = False
        # Set the active bone to "eyebrow_l_down"
        armature.data.bones.active = armature.data.bones["eyebrow_l_down"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        # Get the selected bones
        selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].use_y = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation"].influence = 0.3
        bpy.ops.pose.constraint_add(type='COPY_ROTATION')
        # Get the armature object
        armature = bpy.context.active_object
        # Set the target and pole target of the IK constraint of the "foot_r" bone to the active armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].target = armature
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].subtarget = "eye_l"
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].use_x = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].use_z = False
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].mix_mode = 'AFTER'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].target_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones["eyebrow_l_down"].constraints["Copy Rotation.001"].influence = 0.15
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
        # Set the active bone to "eye_follow_r"
        armature.data.bones.active = armature.data.bones["eye_follow_r"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Index"]
        # Set the active bone to "eye_follow_l"
        armature.data.bones.active = armature.data.bones["eye_follow_l"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_Index"]
        # Set the active bone to "eye_follow"
        armature.data.bones.active = armature.data.bones["eye_follow"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_EyeTrackMid"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 20
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 20
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 20
        # Set the active bone to "Jaw"
        armature.data.bones.active = armature.data.bones["Jaw"]
        # Select the active bone
        bpy.ops.pose.select_all(action='SELECT')
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects["RIG_JawBone"]
        bpy.context.active_pose_bone.custom_shape_scale_xyz[1] = 80
        bpy.context.active_pose_bone.custom_shape_scale_xyz[2] = 80
        bpy.context.active_pose_bone.custom_shape_scale_xyz[0] = 80
        bpy.context.active_pose_bone.custom_shape_rotation_euler[0] = 2.0944
        # Deselect all bones in pose mode
        bpy.ops.pose.select_all(action='DESELECT')
        # Switch to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
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


class SNA_OT_Fix_F_Legs_92244(bpy.types.Operator):
    bl_idname = "sna.fix_f_legs_92244"
    bl_label = "Fix F Legs"
    bl_description = "Fixes Female Legs"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # Switch to pose mode
        bpy.ops.object.mode_set(mode='POSE')
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "foot_r" bone
        bone = obj.pose.bones.get("foot_r")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["foot_r"].constraints["IK"].pole_angle = 0
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "ik_foot_r" bone
        bone = obj.pose.bones.get("ik_foot_r")
        if bone:
            bone.bone.select = True
        bpy.ops.transform.translate(value=(0, 0, 0.212684),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("foot_r")
        if bone:
            bone.bone.select = True
        bpy.ops.transform.rotate(value=5.93992, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("ik_foot_r")
        if bone:
            bone.bone.select = True
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Get the active bone (the one that was selected)
        bone = obj.data.bones.active
        bpy.ops.pose.transforms_clear()
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "calf_r" bone
        bone = obj.pose.bones.get("calf_r")
        if bone:
            bone.bone.select = True
        # Enable limit Z and set IK min Z to 0 on "calf_r" bone
        if bone:
            bone.use_ik_limit_z = True
            bone.ik_min_z = 0
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "ik_foot_l" bone
        bone = obj.pose.bones.get("ik_foot_l")
        if bone:
            bone.bone.select = True
        bpy.ops.transform.translate(value=(0, 0, 0.221244),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("foot_l")
        if bone:
            bone.bone.select = True
        bpy.ops.transform.rotate(value=0.369672, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("ik_foot_l")
        if bone:
            bone.bone.select = True
        bpy.ops.pose.transforms_clear()
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "calf_l" bone
        bone = obj.pose.bones.get("calf_l")
        if bone:
            bone.bone.select = True
        # Enable limit Z and set IK min Z to 0 on "calf_r" bone
        if bone:
            bone.use_ik_limit_z = True
            bone.ik_min_z = 0
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("pelvis")
        if bone:
            bone.bone.select = True
        bpy.ops.transform.translate(value=(-0, -0, -0.396858),   orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("foot_r")
        if bone:
            bone.bone.select = True
        bpy.ops.transform.rotate(value=0.179727, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("foot_l")
        if bone:
            bone.bone.select = True
        bpy.ops.transform.rotate(value=-0.34914, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        # Select "foot_r" bone
        bone = obj.pose.bones.get("pelvis")
        if bone:
            bone.bone.select = True
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Get the active bone (the one that was selected)
        bone = obj.data.bones.active
        bpy.ops.pose.transforms_clear()
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        bpy.ops.object.posemode_toggle()
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)


class SNA_OT_Right_Arm_Fk_88958(bpy.types.Operator):
    bl_idname = "sna.right_arm_fk_88958"
    bl_label = "Right Arm Fk"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "hand_r" bone
        bone = obj.pose.bones.get("hand_r")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["hand_r"].constraints["IK"].influence = 0
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["hand_r"].constraints["IK"].keyframe_insert(data_path="influence")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Right_Arm_Ik_6238D(bpy.types.Operator):
    bl_idname = "sna.right_arm_ik_6238d"
    bl_label = "Right Arm IK"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "hand_r" bone
        bone = obj.pose.bones.get("hand_r")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["hand_r"].constraints["IK"].influence = 1
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["hand_r"].constraints["IK"].keyframe_insert(data_path="influence")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Left_Arm_Fk_Fc07B(bpy.types.Operator):
    bl_idname = "sna.left_arm_fk_fc07b"
    bl_label = "Left Arm Fk"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "hand_l" bone
        bone = obj.pose.bones.get("hand_l")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["hand_l"].constraints["IK"].influence = 0
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["hand_l"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Left_Arm_Ik_34D22(bpy.types.Operator):
    bl_idname = "sna.left_arm_ik_34d22"
    bl_label = "Left Arm Ik"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "hand_l" bone
        bone = obj.pose.bones.get("hand_l")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["hand_l"].constraints["IK"].influence = 1
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["hand_l"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Right_Leg_Fk_A0168(bpy.types.Operator):
    bl_idname = "sna.right_leg_fk_a0168"
    bl_label = "Right Leg Fk"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "foot_r" bone
        bone = obj.pose.bones.get("foot_r")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["foot_r"].constraints["IK"].influence = 0
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["foot_r"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Right_Leg_Ik_95851(bpy.types.Operator):
    bl_idname = "sna.right_leg_ik_95851"
    bl_label = "Right Leg Ik"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "foot_r" bone
        bone = obj.pose.bones.get("foot_r")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["foot_r"].constraints["IK"].influence = 1
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["foot_r"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Left_Leg_Fk001_77D5A(bpy.types.Operator):
    bl_idname = "sna.left_leg_fk001_77d5a"
    bl_label = "Left Leg Fk.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "foot_l" bone
        bone = obj.pose.bones.get("foot_l")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["foot_l"].constraints["IK"].influence = 0
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["foot_l"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Left_Leg_Fk002_9B321(bpy.types.Operator):
    bl_idname = "sna.left_leg_fk002_9b321"
    bl_label = "Left Leg Fk.002"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "foot_l" bone
        bone = obj.pose.bones.get("foot_l")
        if bone:
            bone.bone.select = True
        bpy.context.object.pose.bones["foot_l"].constraints["IK"].influence = 1
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["foot_l"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Right_Eye_Fk001_96C90(bpy.types.Operator):
    bl_idname = "sna.right_eye_fk001_96c90"
    bl_label = "Right Eye Fk.001"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "eye_r" bone
        bone = obj.pose.bones.get("eye_r")
        if bone:
            bone.bone.select = True
        # Set the influence of the "Track To" constraint on "eye_r" bone to 0
        constraint = bpy.context.object.pose.bones["eye_r"].constraints.get("Track To")
        if constraint:
            constraint.influence = 0
        # Create a keyframe for the influence property
        constraint.keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Right_Eye_Ik_592F1(bpy.types.Operator):
    bl_idname = "sna.right_eye_ik_592f1"
    bl_label = "Right Eye Ik"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "eye_r" bone
        bone = obj.pose.bones.get("eye_r")
        if bone:
            bone.bone.select = True
        # Set the influence of the "Track To" constraint on "eye_r" bone to 1
        constraint = bpy.context.object.pose.bones["eye_r"].constraints.get("Track To")
        if constraint:
            constraint.influence = 1
        # Create a keyframe for the influence property
        constraint.keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Left_Eye_Fk_42Bf5(bpy.types.Operator):
    bl_idname = "sna.left_eye_fk_42bf5"
    bl_label = "Left Eye Fk"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "eye_l" bone
        bone = obj.pose.bones.get("eye_l")
        if bone:
            bone.bone.select = True
        # Set the influence of the "Track To" constraint on "eye_l" bone to 0
        constraint = bpy.context.object.pose.bones["eye_l"].constraints.get("Track To")
        if constraint:
            constraint.influence = 0
        # Create a keyframe for the influence property
        constraint.keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Left_Eye_Ik_603A4(bpy.types.Operator):
    bl_idname = "sna.left_eye_ik_603a4"
    bl_label = "Left Eye Ik"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "eye_l" bone
        bone = obj.pose.bones.get("eye_l")
        if bone:
            bone.bone.select = True
        # Set the influence of the "Track To" constraint on "eye_l" bone to 0
        constraint = bpy.context.object.pose.bones["eye_l"].constraints.get("Track To")
        if constraint:
            constraint.influence = 1
        # Create a keyframe for the influence property
        constraint.keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_OW_IK__SXLAR3D_35138(bpy.types.Panel):
    bl_label = 'Ow Ik - Sxlar3d'
    bl_idname = 'SNA_PT_OW_IK__SXLAR3D_35138'
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
        split_DD50B = layout.split(factor=0.5, align=False)
        split_DD50B.alert = False
        split_DD50B.enabled = True
        split_DD50B.active = True
        split_DD50B.use_property_split = False
        split_DD50B.use_property_decorate = False
        split_DD50B.scale_x = 1.0
        split_DD50B.scale_y = 1.0
        split_DD50B.alignment = 'Expand'.upper()
        split_DD50B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = split_DD50B.operator('sna.create_rig_505a9', text='Create Ik Rig', icon_value=0, emboss=True, depress=False)
        op = split_DD50B.operator('sna.fix_f_legs_92244', text='Fix Female Legs', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sn.dummy_button_operator', text='Hide HardPoints (Next Update)', icon_value=0, emboss=True, depress=False)
        layout.label(text='Non Human Characters Unique Rigs', icon_value=172)
        row_39A30 = layout.row(heading='', align=True)
        row_39A30.alert = False
        row_39A30.enabled = True
        row_39A30.active = True
        row_39A30.use_property_split = False
        row_39A30.use_property_decorate = False
        row_39A30.scale_x = 1.0
        row_39A30.scale_y = 1.0
        row_39A30.alignment = 'Expand'.upper()
        row_39A30.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_39A30.label(text='Orisa Ik Rig', icon_value=0)
        op = row_39A30.operator('sna.create_orisa_rig_6b0f4', text='Ik Rig', icon_value=0, emboss=True, depress=False)
        op = row_39A30.operator('sna.orisa_l_back_leg_f1730', text='L Back Leg FK/IK', icon_value=0, emboss=True, depress=False)
        op = row_39A30.operator('sna.orisa_r_back_leg_da9fc', text='R Back Leg FK/IK', icon_value=0, emboss=True, depress=False)
        row_F142A = layout.row(heading='', align=True)
        row_F142A.alert = False
        row_F142A.enabled = True
        row_F142A.active = True
        row_F142A.use_property_split = False
        row_F142A.use_property_decorate = False
        row_F142A.scale_x = 1.0
        row_F142A.scale_y = 1.0
        row_F142A.alignment = 'Expand'.upper()
        row_F142A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_F142A.label(text='Junkrat Ik Rig', icon_value=0)
        op = row_F142A.operator('sna.create_junkrat_rig_af672', text='Ik Rig', icon_value=0, emboss=True, depress=False)
        layout.label(text='Fk/Ik Switch', icon_value=117)
        row_36AF8 = layout.row(heading='', align=True)
        row_36AF8.alert = False
        row_36AF8.enabled = True
        row_36AF8.active = True
        row_36AF8.use_property_split = False
        row_36AF8.use_property_decorate = False
        row_36AF8.scale_x = 1.0
        row_36AF8.scale_y = 1.0
        row_36AF8.alignment = 'Expand'.upper()
        row_36AF8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_36AF8.label(text='Right Arm', icon_value=0)
        op = row_36AF8.operator('sna.right_arm_fk_88958', text='FK', icon_value=0, emboss=True, depress=False)
        op = row_36AF8.operator('sna.right_arm_ik_6238d', text='IK', icon_value=0, emboss=True, depress=False)
        row_42463 = layout.row(heading='', align=True)
        row_42463.alert = False
        row_42463.enabled = True
        row_42463.active = True
        row_42463.use_property_split = False
        row_42463.use_property_decorate = False
        row_42463.scale_x = 1.0
        row_42463.scale_y = 1.0
        row_42463.alignment = 'Expand'.upper()
        row_42463.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_42463.label(text='Left Arm', icon_value=0)
        op = row_42463.operator('sna.left_arm_fk_fc07b', text='FK', icon_value=0, emboss=True, depress=False)
        op = row_42463.operator('sna.left_arm_ik_34d22', text='IK', icon_value=0, emboss=True, depress=False)
        row_5078C = layout.row(heading='', align=True)
        row_5078C.alert = False
        row_5078C.enabled = True
        row_5078C.active = True
        row_5078C.use_property_split = False
        row_5078C.use_property_decorate = False
        row_5078C.scale_x = 1.0
        row_5078C.scale_y = 1.0
        row_5078C.alignment = 'Expand'.upper()
        row_5078C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_5078C.label(text='Right Leg', icon_value=0)
        op = row_5078C.operator('sna.right_leg_fk_a0168', text='FK', icon_value=0, emboss=True, depress=False)
        op = row_5078C.operator('sna.right_leg_ik_95851', text='IK', icon_value=0, emboss=True, depress=False)
        row_769F6 = layout.row(heading='', align=True)
        row_769F6.alert = False
        row_769F6.enabled = True
        row_769F6.active = True
        row_769F6.use_property_split = False
        row_769F6.use_property_decorate = False
        row_769F6.scale_x = 1.0
        row_769F6.scale_y = 1.0
        row_769F6.alignment = 'Expand'.upper()
        row_769F6.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_769F6.label(text='Left Leg', icon_value=0)
        op = row_769F6.operator('sna.left_leg_fk001_77d5a', text='FK', icon_value=0, emboss=True, depress=False)
        op = row_769F6.operator('sna.left_leg_fk002_9b321', text='IK', icon_value=0, emboss=True, depress=False)
        row_192F9 = layout.row(heading='', align=True)
        row_192F9.alert = False
        row_192F9.enabled = True
        row_192F9.active = True
        row_192F9.use_property_split = False
        row_192F9.use_property_decorate = False
        row_192F9.scale_x = 1.0
        row_192F9.scale_y = 1.0
        row_192F9.alignment = 'Expand'.upper()
        row_192F9.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_192F9.label(text='Right Eye', icon_value=0)
        op = row_192F9.operator('sna.right_eye_fk001_96c90', text='FK', icon_value=0, emboss=True, depress=False)
        op = row_192F9.operator('sna.right_eye_ik_592f1', text='IK', icon_value=0, emboss=True, depress=False)
        row_2E683 = layout.row(heading='', align=True)
        row_2E683.alert = False
        row_2E683.enabled = True
        row_2E683.active = True
        row_2E683.use_property_split = False
        row_2E683.use_property_decorate = False
        row_2E683.scale_x = 1.0
        row_2E683.scale_y = 1.0
        row_2E683.alignment = 'Expand'.upper()
        row_2E683.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_2E683.label(text='Left Eye', icon_value=0)
        op = row_2E683.operator('sna.left_eye_fk_42bf5', text='FK', icon_value=0, emboss=True, depress=False)
        op = row_2E683.operator('sna.left_eye_ik_603a4', text='IK', icon_value=0, emboss=True, depress=False)


class SNA_OT_Orisa_R_Back_Leg_Da9Fc(bpy.types.Operator):
    bl_idname = "sna.orisa_r_back_leg_da9fc"
    bl_label = "Orisa R Back Leg"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "foot_r" bone
        bone = obj.pose.bones.get("back_foot_r")
        if bone:
            bone.bone.select = True
        ik_constraint = bpy.context.object.pose.bones["back_foot_r"].constraints["IK"]
        # Toggle the influence value
        if ik_constraint.influence == 0:
            ik_constraint.influence = 1
        else:
            ik_constraint.influence = 0
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["back_foot_r"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Orisa_L_Back_Leg_F1730(bpy.types.Operator):
    bl_idname = "sna.orisa_l_back_leg_f1730"
    bl_label = "Orisa L Back Leg"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        # get the active object
        obj = bpy.context.object
        # check if object is already in pose mode
        if obj.mode == 'POSE':
            print("Object is already in pose mode")
        else:
            # switch to pose mode
            bpy.ops.object.posemode_toggle()
            print("Switched to pose mode")
        # Get the active object (the one that was selected)
        obj = bpy.context.active_object
        # Select "foot_r" bone
        bone = obj.pose.bones.get("back_foot_l")
        if bone:
            bone.bone.select = True
        ik_constraint = bpy.context.object.pose.bones["back_foot_l"].constraints["IK"]
        # Toggle the influence value
        if ik_constraint.influence == 0:
            ik_constraint.influence = 1
        else:
            ik_constraint.influence = 0
        # Create a keyframe for the influence property
        bpy.context.object.pose.bones["back_foot_l"].constraints["IK"].keyframe_insert(data_path="influence")
        # Deselect all bones
        for bone in obj.pose.bones:
            bone.bone.select = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_OT_Create_Orisa_Rig_6B0F4)
    bpy.utils.register_class(SNA_OT_Create_Junkrat_Rig_Af672)
    bpy.utils.register_class(SNA_OT_Create_Rig_505A9)
    bpy.utils.register_class(SNA_OT_Fix_F_Legs_92244)
    bpy.utils.register_class(SNA_OT_Right_Arm_Fk_88958)
    bpy.utils.register_class(SNA_OT_Right_Arm_Ik_6238D)
    bpy.utils.register_class(SNA_OT_Left_Arm_Fk_Fc07B)
    bpy.utils.register_class(SNA_OT_Left_Arm_Ik_34D22)
    bpy.utils.register_class(SNA_OT_Right_Leg_Fk_A0168)
    bpy.utils.register_class(SNA_OT_Right_Leg_Ik_95851)
    bpy.utils.register_class(SNA_OT_Left_Leg_Fk001_77D5A)
    bpy.utils.register_class(SNA_OT_Left_Leg_Fk002_9B321)
    bpy.utils.register_class(SNA_OT_Right_Eye_Fk001_96C90)
    bpy.utils.register_class(SNA_OT_Right_Eye_Ik_592F1)
    bpy.utils.register_class(SNA_OT_Left_Eye_Fk_42Bf5)
    bpy.utils.register_class(SNA_OT_Left_Eye_Ik_603A4)
    bpy.utils.register_class(SNA_PT_OW_IK__SXLAR3D_35138)
    bpy.utils.register_class(SNA_OT_Orisa_R_Back_Leg_Da9Fc)
    bpy.utils.register_class(SNA_OT_Orisa_L_Back_Leg_F1730)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_OT_Create_Orisa_Rig_6B0F4)
    bpy.utils.unregister_class(SNA_OT_Create_Junkrat_Rig_Af672)
    bpy.utils.unregister_class(SNA_OT_Create_Rig_505A9)
    bpy.utils.unregister_class(SNA_OT_Fix_F_Legs_92244)
    bpy.utils.unregister_class(SNA_OT_Right_Arm_Fk_88958)
    bpy.utils.unregister_class(SNA_OT_Right_Arm_Ik_6238D)
    bpy.utils.unregister_class(SNA_OT_Left_Arm_Fk_Fc07B)
    bpy.utils.unregister_class(SNA_OT_Left_Arm_Ik_34D22)
    bpy.utils.unregister_class(SNA_OT_Right_Leg_Fk_A0168)
    bpy.utils.unregister_class(SNA_OT_Right_Leg_Ik_95851)
    bpy.utils.unregister_class(SNA_OT_Left_Leg_Fk001_77D5A)
    bpy.utils.unregister_class(SNA_OT_Left_Leg_Fk002_9B321)
    bpy.utils.unregister_class(SNA_OT_Right_Eye_Fk001_96C90)
    bpy.utils.unregister_class(SNA_OT_Right_Eye_Ik_592F1)
    bpy.utils.unregister_class(SNA_OT_Left_Eye_Fk_42Bf5)
    bpy.utils.unregister_class(SNA_OT_Left_Eye_Ik_603A4)
    bpy.utils.unregister_class(SNA_PT_OW_IK__SXLAR3D_35138)
    bpy.utils.unregister_class(SNA_OT_Orisa_R_Back_Leg_Da9Fc)
    bpy.utils.unregister_class(SNA_OT_Orisa_L_Back_Leg_F1730)
