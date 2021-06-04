resource "tfe_policy_set" "cost_optimization_dev" {
  name          = "CostOptimazation"
  description   = "PolicySets for CostOpmtimazation"
  organization  = var.tfe_org
  policies_path = "policies/cost-optimization"
  workspace_ids = [
      
  ]

  vcs_repo {
    identifier         = "${var.vcs_org}/${var.vcs_repo}"
    branch             = "master"
    ingress_submodules = false
    oauth_token_id     = var.oauth_token_id # this is only an internal id for Terraform Enterprise to specify to use the github connector.
  }
}

resource "tfe_policy_set_parameter" "cost_optimization_dev_max_percentage" {
  key          = "max_percentage"
  value        = "15"
  policy_set_id = tfe_policy_set.cost_optimization_dev.id
}