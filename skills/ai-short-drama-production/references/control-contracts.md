# 短剧可控性合同（含自建实战工程扩展）

仅在对应任务需要时加载本文件。合同可直接写进 `shots.json`、工作单或工程注册表；字段缺失即标记 `pending`。

## 1. narrative_beat_contract

~~~json
{"scene_id":"E01S01","source_form":"script|outline|sketch|oral","assumptions":[],"director_analysis_ref":"","visual_concept_ref":"","hook":"","information_gap":"","actors":[{"asset_id":"C01","want":"","obstacle":"","strategy_shift":"","in_state":"","out_state":""}],"power_turn":"","audience_emotion_curve":[],"cost":"","cliffhanger":"","evidence_shots":[]}
~~~

## 2. asset_registry_entry

~~~json
{"asset_id":"C01","version":"v1.0","status":"approved","reference_images":[],"locked_features":[],"state_variants":[],"used_by_shots":[],"last_reviewed":"YYYY-MM-DD"}
~~~

## 3. voice_anchor_contract（声线锚定资产合同）★

~~~json
{"voice_anchor_id":"VA_Lucas","character_id":"C01","audio_file":"VoxCPM2_EN/normalized/Lucas_VoiceAnchor_v1_EN.wav","h3_label":"<Audio 1>","workflow_input":"ref_audio_0","voice_characteristics":"firm, resonant, youthful baritone with quiet intensity","status":"locked"}
~~~

## 4. immutable_dialogue_ledger（不可变台词防篡改台账）★

~~~json
{"dialogue_id":"D_E01S01_M01_01","scene_id":"E01S01","segment_id":"M01","speaker_asset_id":"C02","original_text":"Moving slow as a dead dog! If this old armor isn't tuned today, you won't even have mud water to drink!","language":"English","time_window_sec":7.5,"word_count":21,"speaking_rate_words_per_sec":2.8,"mouth_visibility":"visible_front_three_quarter|off_screen","h3_tag":"<d>[English] Moving slow as a dead dog! If this old armor isn't tuned today, you won't even have mud water to drink!</d>","status":"locked"}
~~~

## 5. audio_silence_contract（配乐静音隔离协议）★

~~~json
{"non_diegetic_music":"SILENT","rationale":"Isolate AI-generated Foley/soundscape from background music; score must be uniformly laid down on post-production NLE timeline to prevent jarring jump-cuts across segments."}
~~~

## 6. blocking_map（场面调度图）

~~~json
{"blocking_map_id":"BM_E01S01_003","orientation":"screen-left-to-right","space_anchors":{"left":"","mid":"","right":"","foreground":"","background":""},"power_geometry":{"start":"","turn":"","end":""},"axis":{"a":"","b":"","camera_side":""},"beats":[{"id":"T0","actors":[{"asset_id":"C01","position":"left-mid","depth":"mid","facing":"right","eyeline":"C02","entry_exit":"","occlusion":""}],"props":[{"asset_id":"P01","holder":"C01","facing":"","position":""}],"camera":{"position":"","heading":"","lens":"","shot_size":""}},{"id":"T1","changes":[]},{"id":"T2","changes":[]}]}
~~~

## 7. lighting_plan（布光图）

~~~json
{"lighting_plan_id":"LP_E01S01_003","narrative_purpose":"","key":{"source":"","direction":"","kelvin":0,"target":""},"fill":{"source":"","ratio":"","target":""},"rim_or_background":{"source":"","direction":"","target":""},"darkness_purpose":"","continuity":{"T0":"","T2":""},"bans":["no unmotivated glow","no unreadable key action"]}
~~~

## 8. action_ledger（打戏与刚体动作账本）

~~~json
{"action_ledger_id":"AL_E01S01_003","feasibility":{"causal_beats":1,"actor_count":2,"camera_motion":"","decision":"keep|split|offscreen"},"beats":[{"id":"A1","seconds":"0-1.2","initiator":"C01","start":"","path":"","end":"","contact_or_miss":"","reaction":"","screen_direction":"","camera_relation":"","bans":["anti_bounce_continuous_downward_pressure","no_rebounding"]}],"tail_frame":""}
~~~

## 9. sketch_to_shot_brief（草图转镜头）

~~~json
{"sketch_id":"SK01","inherits":{"composition":"","horizon":"","camera_angle":"","subject_scale":"","eyeline":"","key_direction":""},"must_resolve_from_assets":["identity","wardrobe","materials"],"must_resolve_from_style":["palette","texture","lens"],"do_not_inherit":["unapproved face","placeholder text","ambiguous hand detail"]}
~~~

## 10. contact_interaction_sheet（物理接触特写参考合同）★

~~~json
{"contact_id":"CIS_E01S01_M01","initiator":"C02","target":"C01","contact_part":"boot_sole_to_dorsal_hand","prop_id":"P01","reference_image":"01_视觉资产/镜头局部参考/M01_boot_crushing_hand_contact_ref.png","h3_slot":"<Picture 2>","physical_state":"continuous_immovable_downward_pressure","bans":["no_rebounding","no_foot_lifting"],"status":"locked"}
~~~

## 11. QC 对照顺序（终验硬门）

1. **核对声线与不可变台词**：主角发声是否正确映射 `<Audio N>`，台词是否 100% 逐字对应剧本且配乐严格为 `SILENT`。
2. **核对 15 秒动作预算**：铺垫≤2s，冲突2~4s，核心对白4~12s，尾态锁定12~15s，无动作被挤压在片尾。
3. **核对物理接触与 Cxx/Sxx/Pxx**：凡涉肢体对抗者是否绑定接触参考图（`contact_interaction_sheet`）。
4. **核对光源方向、色温与暗部目的**：再核对镜头和 180° 轴线。
5. **对动作逐拍核对**：发力、路径、接触/落空和反应，包含 Anti-Bounce 刚体约束。
6. **核对尾帧交接与音频过渡**：取上一段 `-0.35s` 稳定无黑场关键帧作为下一镜入口；多段拼接施加 `-af acrossfade=d=0.2` 平滑底噪。

