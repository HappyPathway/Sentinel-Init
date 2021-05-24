
data "tfe_workspace" "{{ workspace }}" {
  name         = "{{ workspace.name }}"
  organization = "{{ workspace.organization }}"
}

