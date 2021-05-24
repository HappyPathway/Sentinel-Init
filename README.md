# sentinel-policies
This repo contains all of our Sentinel Policies for Terrafom Enterprise. 
As sentinel can be rather difficult to learn, the hope is that this repo makes 
it a bit easier to begin creating policies. 

## Boilerplate Code
Hashicorp has provided code to help get people started with sentinel, the code in the common-functions directory contains this code.
In each of the directories, you see a docs directory. These docs contain useful information as to how to best leverage this code. 
In order to use this code, you will need to import it into whichever policy set you are workign on. If you look in other directories 
(not utils, we will cover that later), you will see a sentinel.hcl file. These sentinel.hcl files are where you declare your policies
as well as specify the source for included libraries. 

From sentinel.hcl
```hcl
module "tfrun-functions" {
    source = "../common-functions/tfrun-functions/tfrun-functions.sentinel"
}
```

Once you've specified the source of your library, you can include it in your policy. For instance,
```hcl
import "tfrun-functions" as run
```

## Creating New Policies
In order to create a new policy, you'll need to add a new file with the sentinel file extension. 
These policies can be as complex or as simple as you like. The followin is an example of a very simple policy.
```hcl
import "tfrun"
import "decimal"
import "tfrun-functions" as run

param max_percentage default 15

# Main rule
main = rule {
  run.limit_percentage_increase(max_percentage)
}
```

## Paremeterizing Policy
The above policy takes a parameter `max_percentage`. This parameter can be set from outside the policy, thereby allowing you to parameterize 
your policy and enabling you to keep your code DRY (dont repeat yourself). This policy can now be applied to different workspaces without having
to duplicate your code.


## Apply Policy to Specific Workspaces
In order to apply policy to workspaces, you need to define a policy set. These policy sets work in such a way that anything included in your sentinel.hcl
file is automatically applied to the workspace. You can create multiple policy sets that leverage the same policies but have different policy set parameters attached. You can look at cost-optimization.tf as an example. This policy set uses the code in the cost-optimization directory to apply policy. Since the policy in link_percentage_increase.sentinel uses a parameter, there is nothing stopping me from creating another policy set that specifies a different parameter for the workspaces that will be attached to this new policy set. 


## utils directory
This directory contains useful scripts to help create terraform code for deploying policies into place. Currently, there's only one script `list_workspaces.py`, but over time there will be more. These scripts interact with the TFE provider using a custom Python Library
```bash
https://github.com/HappyPathway/PyTFE-Core
```
Git clone this library and then install locally by running 
```bash
python setup.py install
```
Once you have this library, you'll be able to run these scripts.