## can-i
kubectl auth can-i create secrets --namespace kube-system
## ABAC -> RBAC porting
--authorization-mode=RBAC,ABAC --authorization-policy-file=abac-legacy-policy.json