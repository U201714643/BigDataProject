# hadoop数据分析项目

## motivation

> 2015 年，我们尝试在阿里巴巴的数据中心，将延迟不敏感的批量离线计算任务和延迟敏感的在线服务部署到同一批机 器上运行，让在线服务用不完的资源充分被离线使用以提高机器的整体利用率。经过 3 年多的试验论证、架构调整和 资源隔离优化，目前这个方案已经走向大规模生产。我们通过混部技术将集群平均资源利用率从 10% 大幅度提高到 45%。另外，通过各种优化手段，可以让更多任务运行在数据中心，将“双11”平均每万笔交易成本下降了 17%，等等。
[alibaba数据中心](https://www.cnblogs.com/yunqishequ/p/10168748.html)

## 系统部署方式

略

## 数据
### 来源
[alibaba cluster data](https://github.com/alibaba/clusterdata/blob/master/cluster-trace-v2018/trace_2018.md) 

### 数据构成
* machine_meta.csv：the meta info and event infor of machines.
* machine_usage.csv: the resource usage of each machine.
* container_meta.csv：the meta info and event infor of containers.
* container_usage.csv：the resource usage of each container.
* batch_instance.csv：inforamtion about instances in the batch workloads.
* batch_task.csv：inforamtion about instances in the batch workloads. Note that the DAG information of each job's tasks is described in the task_name field.
以下内容见介绍2.3部分，讲了
A complete batch computation job can be described using "job-task-instance" model. We will describe the meaning of each term and how the DAG information is expressed in the trace.

A job is typically consisted of several tasks whose depencies are expressed by DAG (Directed Acyclic Graph). Each task has a number of instances, and only when all the instances of a task are completed can a task be considered as "finished", i.e. if task-2 is depending on task-1, any instance of task-2 cannot be started before all the instances of task-1 are completed. The DAG of tasks in a job can be deduced from the task_name field of all tasks of this job, and it is explained with the following example.

### 数据说明
以下内容见[schema](https://github.com/alibaba/clusterdata/blob/master/cluster-trace-v2018/schema.txt)

这个数据集我们主要使用batch_task 和batch_instance，对应的内容说明如下

#### batch task
+------------------------------------------------------------------------------------+
| task_name       | string     |       | task name. unique within a job              |
| instance_num    | bigint     |       | number of instances                         |
| job_name        | string     |       | job name                                    |
| task_type       | string     |       | task type                                   |
| status          | string     |       | task status                                 |
| start_time      | bigint     |       | start time of the task                      |
| end_time        | bigint     |       | end of time the task                        |
| plan_cpu        | double     |       | number of cpu needed by the task, 100 is 1 core |
| plan_mem        | double     |       | normalized memorty size, [0, 100]           |

### batch instance
| instance_name   | string     |       | instance name of the instance               |
| task_name       | string     |       | name of task to which the instance belong   |
| job_name        | string     |       | name of job to which the instance belong    |
| task_type       | string     |       | task type                                   |
| status          | string     |       | instance status                             |
| start_time      | bigint     |       | start time of the instance                  |
| end_time        | bigint     |       | end time of the instance                    |
| machine_id      | string     |       | uid of host machine of the instance         |
| seq_no          | bigint     |       | sequence number of this instance            |
| total_seq_no    | bigint     |       | total sequence number of this instance      |
| cpu_avg         | double     |       | average cpu used by the instance, 100 is 1 core  |
| cpu_max         | double     |       | average memory used by the instance (normalized) |
| mem_avg         | double     |       | max cpu used by the instance, 100 is 1 core      |
| mem_max         | double     |       | max memory used by the instance (normalized, [0, 100]) |
### 分析方法



主要采取论文 [Learning from failure across multiple clusters : A trace-driven approach to understanding , predicting , and mitigating job terminations](https://ieeexplore.ieee.org/abstract/document/7980073/)
内描述的分析方法， 对集群服务器中大量出现的不成功执行任务提取其特征 
section I.introdution
>  We provide a detailed characterization of factors that dif- ferentiate 
> unsuccessful from successful job executions (Sec- tion III) and explore different 
> hypotheses for root causes that might explain unsuccessful executions (Section
注：我们只利用本论文的 characterization 部分来分析目标数据， 后面的两部分工作不做

#### WHAT CHARACTERIZES UNSUCCESSFUL JOBS IN LARGE CLUSTERS
对于这个问题，有三个特征：

一个job由一个或多个task组成。分为multi-task job和single-task job
1. job duration
通过batch_task中的end_time-start_time可以得到每一个task的持续时间，而要计算job duration则要取没有个job中开始最早的task的start-time和开始最晚的end-time做差得到
job分类：含有Failed的task归为Failed类

分以下三类统计平均时长：通过batch task中的status分类

Terminated 
Failed  
Running 


2. degree of parallelism
通过计算batch instance中一个job对应的task数量来衡量是否是并行计算，区分multi-task job和single-task job
对两类工作比较他们中status不同值的比例，平均运行时间长短。
一个job的运算时间=待定




3. usage of cluster resources
画出不同类型的工作预先请求的资源量的平均值，比较大小
在本数据batch task中有 plan_cpu plan_mem 两个变量可以直接用来比较


### mapreduce code method

#### jobduration 
file:   mapper_start->print line {job_name}  {start_time}    
        reducer_start->combine the pair by selecting the smaller start_tima
        mapper_end->print line {job_name}  {end_time}
        reducer_start->combine the pair by selecting the bigger end_time
        reducer_total->combine the 


        
