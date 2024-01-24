# oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration

原文出处： [《When leading by example leads to less corrupt collaboration》](https://www.sciencedirect.com/science/article/abs/pii/S0167268121001931)
## 1 实验范式

- 来源：摇骰子【die-rolling paradigm】(Fischbacher and Föllmi-Heusi, 2013; Weisel and Shalvi, 2015).
- 参与者 i 的实验任务是私下滚动一个公平的六面骰子，观察其结果，并在计算机屏幕上报告结果 $r_i$。
- 骰子上的数字范围为1、2和3，每个数字在相对的两侧出现，使得掷骰子的实际结果 $o_i$∈{1,2,3}，同时满足P($o_i$=k)=1/3，k∈{1,2,3}。
- 需要注意的是，被试掷骰子的实际结果$o_i$与他报告的结果$r_i$并非一定是相等的
- 骰子并非是计算机模拟，而是真实存在的，但此处为了更好的游戏体验，用计算机模拟生成了一个骰子点数
    
    > *To ensure maximal privacy regarding the outcome of the die roll, dice were placed in lidded cups. The lid had a hole so that only the person sitting in the cubicle could observe the die-roll outcome. All subjects received the same paper instructions that were distributed at a stage-by-stage basis.*
    > 

## 2 实验流程

- **该实验由三个阶段组成（Stage 1-3）**，被试在完成前一个阶段的实验后才能阅读下一阶段的实验指引。实验结束时随机抽取一个阶段作为支付被试报酬的依据。每次实验（Per experimental session）有18-21名被试

### 2.1 Stage 1 (“Individual - One-shot”)

- 共一轮，每位被试单独玩掷骰子游戏并汇报结果，并获得 $3*(r_i-1)$的报酬
  ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/66d75b98-43a4-478d-a504-cfcb0b2baeae)
- 之后，他们通过回答以下问题来陈述他们对其他人行为的看法：*“这个房间里有多少其他受试者输入数字1/2/3 作为他们的结果？* 被试可以输入任何介于0和其他参与者人数之间的数字。
    

    > *Belief elicitation was incentivized. 
    Subjects received an additional 1 € if their estimation deviated by less than 1 unit from the mean of other subjects actual reports. 
    Feedback regarding the correct estimation of their beliefs was given only at the end of the experiment.*
     > 
![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/c9dce892-d82c-4bee-b652-4e0d7572bfdd)

- 目的：测量个人的撒谎倾向，并作为个体控制变量



### 2.2 Stage 2 (“Group - One-Shot”)

- 实验共一轮，受试者被随机分配到三人小组中，在接下来的实验中（stage 2-3）该三人组成员保持不变。
    
  
    > *To avoid effects of framing or context, we keep the role descriptions neutral in the instructions by calling them the “first”, “second”, and “third” group member, respectively. In the paper, we will refer to them as first, second, or third movers, respectively.*
     > 
    
- 同样，每个受试者都有自己的骰子，他需要掷出骰子、观察结果、在屏幕上报告
- 他获得的报酬取决于他的报告内容：当且仅当所有组员都报告了相同的数字，即报告了三连号时，受试者才能获得正报酬。
    - 当报告三连号 1 时，每个组员可获得 30 个代币；
    - 报告三连号 2 时，可获得 60 个代币；
    - 报告三连号 3 时，可获得 90 个代币；
    - 反之，则为 0 个代币。
  ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/648b6407-9855-4445-8c7c-720f3537b782)
- 在所有受试者完成第二阶段后，他们会收到小组中各数字报告情况以及小组报酬的反馈（ the reported individual numbers and the payoffs in their group. ）。但由于掷骰子是不公开的，因此受试者不会收到关于其他人掷骰子结果的反馈。
- 目的：了解一次性群体互动中的说谎倾向

### 2.3 Stage 3 (”Group - Repeated”)

- 实验为连续的5期，受试者在与Stage 2相同的三人小组（同时决策的结构也相同），实验程序与第二阶段相同
- 每轮结束后，被试所获得的报酬情况如下，每轮为Stage 2的1/5：
    - 如果所有组员都报告 1，则每期报酬为 6 个代币；
    - 如果所有组员都报告 2，则每期报酬为 12 个代币；
    - 如果所有组员都报告 3，则每期报酬为 18 个代币；
    - 否则，每期报酬为 0 个代币
- 每期结束后，受试者都会看到自己所在小组中个人所报告的数字和所得报酬的概览（而不是其他人掷骰子的实际结果）。
- 目的：通过重复互动来扩展第二阶段的背景，通过比较第二阶段和第三阶段的行为，我们可以推断出重复互动的重要性。

## 3 实验处理条件

- 实验中有三种处理条件，Stage1 中各处理组都是一样的，只是在Stage 2和Stage 3时有所差别。包括Simultaneous（同时）, Partially Sequential（部分顺序）, and Fully Sequential（完全顺序）：

    - **In the Simultaneous treatment (our baseline)** all three group members simultaneously roll their dice and report their outcome without knowing the reports of the other triad members.【在 "同时处理"（我们的基线）中，三位小组成员同时掷骰子并报告其结果。注意，他们在决策时并不知道小组中其他人的报告内容】

    - **In Partially Sequential**, one member of each triad is chosen randomly and assigned to the role of the first mover, and has to roll and report the die-roll outcome before the other two group members do so. The other two players —thesecond movers —areinformed of the first-mover’s report before they (simultaneously) roll and report themselves without knowing what the respective other second mover reports【在 "部分顺序 "游戏中，三位小组成员中的一名成员被随机选中，并被指派为 "先行者"，他必须在其他两名小组成员行动前，掷骰子并报告结果。另外两名参与者——第二推动者——在（同时）掷骰并报告自己的结果之前，会被告知第一推动者的报告情况，而不知道其他第二推动者的报告】
      - 第一行动者
            ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/458f51fc-a9c5-4885-b797-714dfdf234a7)
            ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/57c7916d-0ff1-4b95-bff1-3c2ee17b401a)
      - 第二行动者
            ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/b401de6c-d3b9-40ab-95a3-ab9f6ba499a1)
            ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/8471f958-7d4b-415b-9bb0-093d90b2c3d1)

    - **In Fully Sequential**, the first mover rolls and reports to the second mover, who is also exogenously selected in each group. The second mover rolls and reports to the third mover. Finally, the third mover is informed about the reports of the first and second movers and rolls and reports herself. 【在 "完全序列 "中，第一行动者掷骰子并向第二行动者报告，接着，第二行动者掷骰子并向第三行动者报告。最后，第三行动者获悉第一位和第二位行动者的报告后，自己掷骰子和报告】
      - 第一行动者
      ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/2be8dd38-07af-47e2-b4a3-68b1467d5cf3)
![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/ef535d37-39bd-4e11-b089-a753e38f3246)
      - 第二行动者
      ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/c781fade-5315-49fc-a29f-3c578e7c8a0c)
![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/82e9b618-97dc-4d38-b752-fcd2a06a1026)

      - 第三行动者
      ![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/40fd6365-32e6-4256-b79f-fb8c29d21aeb)
![image](https://github.com/MaYutao0424/oTree-Implementation-of-Journal-Replication---JEBO---Corrupt-Collaboration/assets/90327043/2d301661-370e-44be-a969-75b520727e88)
