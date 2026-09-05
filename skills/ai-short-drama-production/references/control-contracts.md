# 短剧可控性合同（含自建实战工程扩展）

仅在对应任务需要时加载本文件。合同可直接写进 `shots.json`、工作单或工程注册表；字段缺失即标记 `pending`。

## 1. narrative_beat_contract

~~~json
{"scene_id":"E01S01","source_form":"script|outline|sketch|oral","assumptions":[],"director_analysis_ref":"","visual_concept_ref":"","hook":"","information_gap":"","actors":[{"asset_id":"C01","want":"","obstacle":"","strategy_shift":"","in_state":"","out_state":""}],"power_turn":"","audience_emotion_curve":[],"cost":"","cliffhanger":"","evidence_shots":[]}
~~~

## 2. asset_registry_entry（含粒度分级与法线死锁）★

~~~json
{"asset_id":"C01_Palm","version":"v1.0","status":"approved","granularity_tier":"close_up_part|macro_prop|full_body","reference_images":["Prop_Lucas_Dragonfire_Palm.png"],"locked_features":["concave_inner_palm_rune"],"normal_lock":"camera_faces_directly_into_inner_palm","unmutated_skin_bans":["wrist_and_forearm_100pct_normal_human_skin","zero_magma_veins_on_arm"],"state_variants":[],"used_by_shots":[],"last_reviewed":"YYYY-MM-DD"}
~~~

## 3. voice_anchor_contract（声线锚定资产合同）★

~~~json
{"voice_anchor_id":"VA_Lucas","character_id":"C01","audio_file":"VoxCPM2_EN/normalized/Lucas_VoiceAnchor_v1_EN.wav","h3_label":"<Audio 1>","workflow_input":"ref_audio_0","voice_characteristics":"firm, resonant, youthful baritone with quiet intensity","status":"locked"}
~~~

## 4. immutable_dialogue_ledger（不可变台词防篡改台账 · 含闭嘴死锁与因果验证）★

~~~json
{"dialogue_id":"D_E01S01_M01_01","scene_id":"E01S01","segment_id":"M01","speaker_asset_id":"C02","original_text":"Moving slow as a dead dog! If this old armor isn't tuned today, you won't even have mud water to drink!","language":"English","time_window_sec":7.5,"word_count":21,"speaking_rate_words_per_sec":2.8,"mouth_visibility":"visible_front_three_quarter|off_screen","speaker_facing_priority":"dominant_foreground","non_speakers_muzzle_lock":"lips_tightly_pressed_shut_zero_movement","causality_verified":"action_first_then_gaze_then_dialogue","h3_tag":"<d>[English] Moving slow as a dead dog! If this old armor isn't tuned today, you won't even have mud water to drink!</d>","status":"locked"}
~~~

## 5. audio_silence_contract（配乐静音隔离协议）★

~~~json
{"non_diegetic_music":"SILENT","rationale":"Isolate AI-generated Foley/soundscape from background music; score must be uniformly laid down on post-production NLE timeline to prevent jarring jump-cuts across segments."}
~~~

## 6. blocking_map（场面调度图 · 含第0秒刚体常驻）★

~~~json
{"blocking_map_id":"BM_E01S01_003","orientation":"screen-left-to-right","space_anchors":{"left":"","mid":"","right":"","foreground":"","background":""},"anchor_zero_props":[{"prop_id":"P_Gears","location":"screen_left_foreground_mud","presence_from_sec":"00:00.000","bans":["no_spawning_out_of_thin_air"]}],"power_geometry":{"start":"","turn":"","end":""},"axis":{"a":"","b":"","camera_side":""},"beats":[{"id":"T0","actors":[{"asset_id":"C01","position":"left-mid","depth":"mid","facing":"right","eyeline":"C02","entry_exit":"","occlusion":""}],"props":[{"asset_id":"P01","holder":"C01","facing":"","position":""}],"camera":{"position":"","heading":"","lens":"","shot_size":""}},{"id":"T1","changes":[]},{"id":"T2","changes":[]}]}
~~~

## 7. lighting_plan（布光图）

~~~json
{"lighting_plan_id":"LP_E01S01_003","narrative_purpose":"","key":{"source":"","direction":"","kelvin":0,"target":""},"fill":{"source":"","ratio":"","target":""},"rim_or_background":{"source":"","direction":"","target":""},"darkness_purpose":"","continuity":{"T0":"","T2":""},"bans":["no unmotivated glow","no unreadable key action"]}
~~~

## 8. action_ledger（打戏与刚体动作账本 · 含状态闭环与跳切）★

~~~json
{"action_ledger_id":"AL_E01S01_003","feasibility":{"causal_beats":1,"actor_count":2,"camera_motion":"","decision":"keep|split|offscreen"},"action_state_machine":{"lifecycle":"open_execute_close_complete","finish_action":"slam_receiver_onto_cradle_before_cut"},"costume_change_protocol":{"in_shot_morph_ban":true,"required_transition":"hard_cut_or_match_cut_only"},"beats":[{"id":"A1","seconds":"0-1.2","initiator":"C01","start":"","path":"","end":"","contact_or_miss":"","reaction":"","screen_direction":"","camera_relation":"","bans":["anti_bounce_continuous_downward_pressure","no_rebounding"]}],"tail_frame":""}
~~~

## 9. sketch_to_shot_brief（草图转镜头）

~~~json
{"sketch_id":"SK01","inherits":{"composition":"","horizon":"","camera_angle":"","subject_scale":"","eyeline":"","key_direction":""},"must_resolve_from_assets":["identity","wardrobe","materials"],"must_resolve_from_style":["palette","texture","lens"],"do_not_inherit":["unapproved face","placeholder text","ambiguous hand detail"]}
~~~

## 10. QC 对照顺序（工业实战终验硬门）★

1. **核对资产粒度与拍摄法线**：特写/局部镜头是否绑定局部专用微距资产卡？是否锁死拍摄法线并排他约束周边正常人体皮肤？
2. **核对声线与闭嘴死锁**：发声角色是否主控画框，非发声角色是否嘴唇紧闭（lips tightly pressed shut）？主角正确映射 `<Audio N>`，配乐严格 `SILENT`。
3. **核对视听因果递进**：台词是否发生在“动作完成”与“视线注视”之后？绝无未见先知的发问。
4. **核对第 0 秒刚体常驻**：中途捡拾/交互的道具是否从 00:00.000 就已客观存在于场景绝对坐标？绝无虚空刷新。
5. **核对动作闭环与换装跳切**：交互动作是否有头有尾（如电话重扣挂断）？换装是否采用硬切独立镜头，绝无单镜内变装。
6. **核对 Cxx/Sxx/Pxx 与调度轴线**：与批准版本一致，核对 180° 轴线与 T0、T1、T2 调度。
7. **对动作逐拍核对**：发力、路径、接触/落空和反应，包含 Anti-Bounce 刚体约束。
8. **核对尾帧交接**：取上一段 `-0.35s` 稳定无黑场关键帧作为下一镜入口。

