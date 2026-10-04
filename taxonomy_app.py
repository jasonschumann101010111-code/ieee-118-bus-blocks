from dataclasses import dataclass, field
from typing import List
import json


@dataclass
class TaxonomyNode:
    name: str
    description: str
    children: List["TaxonomyNode"] = field(default_factory=list)

    def render(self, indent: int = 0) -> None:
        print("  " * indent + f"- {self.name}: {self.description}")
        for child in self.children:
            child.render(indent + 1)

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "children": [child.to_dict() for child in self.children],
        }


def build_ai_taxonomy() -> TaxonomyNode:
    return TaxonomyNode(
        "Artificial Intelligence (AI)",
        "Computational systems designed to perform intelligent tasks",
        children=[
            TaxonomyNode(
                "Machine Learning (ML)",
                "Algorithms that learn patterns from data",
                children=[
                    TaxonomyNode(
                        "Deep Learning (DL)",
                        "Multi-layered artificial neural networks",
                        children=[
                            TaxonomyNode(
                                "Generative AI (GenAI)",
                                "Models that create new content such as text, code, images, and audio",
                            )
                        ],
                    )
                ],
            )
        ],
    )


def main() -> None:
    taxonomy = build_ai_taxonomy()
    print("AI Taxonomy Explorer")
    print("=" * 24)
    taxonomy.render()
    print("\nJSON Structure:")
    print(json.dumps(taxonomy.to_dict(), indent=2))


if __name__ == "__main__":
    main()
