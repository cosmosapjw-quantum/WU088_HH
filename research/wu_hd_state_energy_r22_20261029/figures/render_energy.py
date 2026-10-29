"""Source-family contrast, not an observed confidence interval or physical heat plot."""
from pathlib import Path
import json
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
case=json.loads((root/'results'/'CASE_105_255.json').read_text())
rows=case['candidates']
labels=['Neutral 2021\n(no IP offset)','2019 ground +\n2021 rotations','2021 levels +\n2019 IP offset']
thresholds=[float(x['threshold_meV_exact_literal']) for x in rows]
fig,ax=plt.subplots(figsize=(7.3,4.0))
ax.bar(labels,thresholds)
ax.set_ylabel('Conditional reaction threshold (meV)')
ax.set_title('Cross-paper source conventions, not physical uncertainty')
ax.set_ylim(0,25)
for i,v in enumerate(thresholds):ax.text(i,v+0.3,f'{v:.7f}',ha='center',fontsize=9)
fig.tight_layout();fig.savefig(root/'figures'/'R22_THRESHOLD_CONTRAST.png',dpi=175);plt.close(fig)

intercept=float(case['caloric_model']['affine_bath_delta_per_reference_m3']['intercept_J_per_ref_m3'])
contrib=[float(x['diagnostic_Q_times_extent_J_per_reference_m3']) for x in rows]
fig,ax=plt.subplots(figsize=(7.3,4.2))
ax.bar(labels,[x/1e-15 for x in contrib])
ax.axhline(intercept/1e-15,linestyle='--',linewidth=1.2)
ax.text(0.02, intercept/1e-15+0.22, 'Known bath intercept (Q independent)',fontsize=9,ha='left')
ax.set_ylabel('Energy / reference volume (10⁻¹⁵ J m⁻³)')
ax.set_title('R21 affine-heat sensitivity, conditional source mismatch')
ax.set_ylim(-7.1,0.4)
fig.tight_layout();fig.savefig(root/'figures'/'R22_ENERGY_COEFFICIENTS.png',dpi=175);plt.close(fig)
print('FIGURE FILES:',*(p.name for p in sorted((root/'figures').glob('*.png'))))
